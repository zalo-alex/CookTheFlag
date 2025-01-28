from pathlib import Path
from flask import Flask, render_template, request, redirect, flash
from flask_sock import Sock
from flask_migrate import Migrate
from types import GeneratorType

from src.module_manage import ModuleManage
from src.files import Files
from src.models import db, User
from src.auth import is_logged, auth_route, set_user_session

import base64
import json
import os
import traceback
import string
import random

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite' # TODO: Should use the volume for docker !
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = os.urandom(24)

db.init_app(app)
migrate = Migrate(app, db)

sock = Sock(app)

manager = ModuleManage()
files = Files()

def init_cook_user():
    charset = string.ascii_uppercase + string.digits
    password = f"{''.join(random.choices(charset, k=3))}-{''.join(random.choices(charset, k=4))}"

    with app.app_context():
        cook_user = User.query.filter_by(username="cook").one_or_none()
        if cook_user:
            db.session.delete(cook_user)
            db.session.commit()
        
        cook_user = User(username="cook")
        cook_user.set_password(password)

        db.session.add(cook_user)
        db.session.commit()

    print(f" ! Temp Cook Account: cook:{password}")

@app.errorhandler(404) 
def not_found(e): 
    return render_template("404.html", modules=manager.modules, categories=manager.categories) 

@app.route("/")
def index():
    return render_template("index.html", modules=manager.modules, categories=manager.categories)

@app.route("/files")
def files_view():
    path = files.get_path(request.args.get("path", ".")) 

    if not files.exists(path):
        return render_template("files.html", path=path, folders=[], files=[], downloadables=[], modules=manager.modules, categories=manager.categories, exists=False)
    
    if files.is_dir(path):
        folders, _files = files.list_dir(path)
        # downloadables = files.get_downloadables(path) TODO: Implement downloadables feature
        
        return render_template("files.html", path=path, folders=folders, files=_files, downloadables=[], modules=manager.modules, categories=manager.categories, exists=True)
    else:
        file = files.open(path)
        lines = len(file.readlines())
        file.seek(0)
        preview = files.open(path).read(2048)

        return render_template("file.html", path=path, lines=lines, filename=files.basename(path), modules=manager.modules, preview=preview, categories=manager.categories)

@app.route("/files/upload", methods=["POST"])
def files_upload():    
    path = files.get_path(request.args.get("path", "."))

    if not files.exists(path):
        return redirect(f"/files?path={request.args.get('path', '.')}")
    
    _files = request.files.getlist("files")
    
    for file in _files:
        files.save_file(path, file)

    return redirect(f"/files?path={request.args.get('path', '.')}")

@app.route("/files/delete", methods=["POST"])
def files_delete():    
    path = files.get_path(request.args.get("path", "."))

    if not files.exists(path):
        return redirect(f"/files?path={request.args.get('path', '.')}")
    
    files.delete_file(path)

    return redirect(f"/files?path={os.path.dirname(path)}")

@app.route("/regex/<b64_query>")
def regex(b64_query):
    query = base64.b64decode(b64_query.encode()).decode()
    matches = []

    for r in manager.regexs:
        regex = r["regex"]

        if regex.match(query):
            module = r["module"]
            matches.append({
                "url": module.url,
                "name": module.name,
                "id": r.get("id"),
                "element_name": r.get("element_name")
            })
        
    return {
        "matches": matches
    }

@app.route("/admin")
@auth_route
def admin():
    users = User.query.all()
    return render_template("admin.html", modules=manager.modules, categories=manager.categories, users=users)

@app.route("/admin/user/create", methods=["POST"])
@auth_route
def admin_user_create():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        flash("Username and password are required.", "danger")
        return redirect("/admin")

    if User.query.filter_by(username=username).first():
        flash("Username already exists.", "danger")
        return redirect("/admin")

    user = User(username=username)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    flash("User registered successfully.", "info")
    return redirect("/admin")

@app.route("/login", methods=["GET", "POST"])
def login():
    
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("Username and password are required.", "danger")
            return redirect("/login")
        
        user = User.query.filter_by(username=username).one_or_none()
        if not user:
            flash("Username not found.", "danger")
            return redirect("/login")
        
        if not user.check_password(password):
            flash("Invalid password.", "danger")
            return redirect("/login")

        set_user_session(user)
        flash(f"Logged as {user.username}", "info")
        return redirect("/login")

    return render_template("login.html", modules=manager.modules, categories=manager.categories)

@sock.route('/ws')
def ws(sock):
    logged = is_logged()
    while True:
        payload = json.loads(sock.receive())
        type = payload.get("type")
        payload = payload.get("payload")
        
        if not type or not payload:
            continue
        
        if type == "submit":

            if not logged:
                sock.send(json.dumps({
                    "type": "error", "data": "Unauthorized"
                }))
                continue

            module = payload.get("module")
            if not module or module not in manager.modules:
                continue
            
            module = manager.modules[module]            
            type = payload.get("type")
            data = payload.get("data")
            
            for element in module.layout:
                if element.parser:
                    data[element.id] = element.parser.parse(data[element.id])
            
            try:
                res = module.submit(type, data)
                
                if isinstance(res, GeneratorType):
                    for r in res:
                        sock.send(json.dumps({
                            "type": "response", "data": r
                        }))
                    sock.send(json.dumps({"type": "done"}))
                else:
                    sock.send(json.dumps({
                        "type": "response", "data": res
                    }))
                    sock.send(json.dumps({"type": "done"}))
            except Exception as e:
                traceback.print_exc()
                return {"__error": str(e)}

if __name__ == "__main__":
    manager.import_all(app)
    app.run(host="0.0.0.0", port=8080, debug=True)
