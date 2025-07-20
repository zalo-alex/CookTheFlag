from pathlib import Path
from flask import Flask, render_template, request, redirect, flash
from flask_sock import Sock
from flask_migrate import Migrate
from types import GeneratorType

from src.module_manage import ModuleManage
from src.files import Files
from src.models import db, User
from src.auth import is_logged, auth_route, set_user_session
from src.globals import data_dir
from src.api import api
from src.tasks import Tasks
from src.websocket import ws_clients

import base64
import json
import os
import traceback
import string
import random

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{os.path.join(data_dir, "db.sqlite")}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = os.urandom(24)

app.register_blueprint(api)

db.init_app(app)
migrate = Migrate(app, db)

sock = Sock(app)

manager = ModuleManage()
files = Files()

def init_cook_user():
    with app.app_context():
        cook_user = User.query.filter_by(username="cook").one_or_none()
        if cook_user:
            return
        
        cook_user = User(username="cook")
        cook_user.set_password("cook")
        cook_user.change_password = True

        db.session.add(cook_user)
        db.session.commit()
    
@app.context_processor
def inject_globals():
    return {
        "modules": manager.modules, 
        "categories": manager.categories,
        "running_tasks": Tasks.amount()
    }

@app.errorhandler(404) 
def not_found(e): 
    return render_template("404.html") 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/files")
@auth_route
def files_view():
    path = files.get_path(request.args.get("path", ".")) 

    if not files.exists(path):
        return render_template("files.html", path=path, folders=[], files=[], downloadables=[], exists=False)
    
    if files.is_dir(path):
        folders, _files = files.list_dir(path)
        # downloadables = files.get_downloadables(path) TODO: Implement downloadables feature
        
        return render_template("files.html", path=path, folders=folders, files=_files, downloadables=[], exists=True)
    else:
        file = files.open(path)
        try:
            lines = len(file.readlines())
            file.seek(0)
            preview = files.open(path).read(2048)
        except:
            lines = 0
            preview = "Cannot read file"

        return render_template("file.html", path=path, lines=lines, filename=files.basename(path), modules=manager.modules, preview=preview, categories=manager.categories)

@app.route("/files/upload", methods=["POST"])
@auth_route
def files_upload():    
    path = files.get_path(request.args.get("path", "."))

    if not files.exists(path):
        return redirect(f"/files?path={request.args.get('path', '.')}")
    
    _files = request.files.getlist("files")
    
    for file in _files:
        files.save_file(path, file)

    return redirect(f"/files?path={request.args.get('path', '.')}")

@app.route("/files/delete", methods=["POST"])
@auth_route
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
    return render_template("admin.html", users=users)

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
        
        if user.change_password:
            return redirect(f"/change-password/{user.username}")

        set_user_session(user)
        flash(f"Logged as {user.username}", "info")

        # This should be fixed to prevent open redirects
        return redirect(request.args.get("next") or "/admin")

    return render_template("login.html")

@app.route("/change-password/<username>", methods=["GET", "POST"])
def change_password_username(username):
    user = User.query.filter_by(username=username).one_or_none()
    if not user:
        flash(f'Username "{username}" not found.', "danger")
        return render_template("change-password.html", username=username)

    if request.method == "POST":

        old_password = request.form.get("oldPassword")
        new_password = request.form.get("newPassword")
        confirm_password = request.form.get("confirmPassword")

        if not old_password or not new_password or not confirm_password:
            flash("All fields are required.", "danger")
            return redirect(f"/change-password/{username}")
        
        if new_password != confirm_password:
            flash("Passwords do not match.", "danger")
            return redirect(f"/change-password/{username}")
        
        if user.check_password(old_password):
            flash("Password changed successfully.", "info")
            user.set_password(new_password)
            user.change_password = False
            db.session.commit()
            return redirect(f"/login")
        else:
            flash("Invalid old password.", "danger")
            return redirect(f"/change-password/{username}")
    
    return render_template("change-password.html", username=username)

@app.route("/tasks")
@auth_route
def tasks():
    return render_template("tasks.html", tasks=Tasks.all)

@app.route("/tasks/stop", methods=["POST"])
@auth_route
def tasks_stop():
    task_id = request.args.get("id")
    if not task_id or task_id not in Tasks.all:
        return redirect("/tasks")
    Tasks.stop(Tasks.all[task_id])
    return redirect("/tasks")

@sock.route('/ws')
@auth_route
def ws_route(ws):
    ws_clients.append(ws)

    while True:
        payload = json.loads(ws.receive())
        type = payload.get("type")
        payload = payload.get("payload")
        
        if not type or not payload:
            continue
        
        if type == "submit":

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
                        ws.send(json.dumps({
                            "type": "response", "data": r
                        }))
                    ws.send(json.dumps({"type": "done"}))
                else:
                    ws.send(json.dumps({
                        "type": "response", "data": res
                    }))
                    ws.send(json.dumps({"type": "done"}))
            except Exception as e:
                traceback.print_exc()
                ws.send(json.dumps({
                    "type": "response", "data": {"__error": str(e)}
                }))

if not os.environ.get("FLASK_DB_MIGRATION"):
    manager.import_all(app)
    init_cook_user()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
