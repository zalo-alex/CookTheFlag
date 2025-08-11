from flask import Blueprint, request, redirect, url_for

from src.files import Files
from src.auth import logged_route, admin_route
from src.models import db, User

files = Files()

api = Blueprint("api", __name__, url_prefix="/api")

@api.route("/files")
@logged_route
def api_files():
    path = files.get_path(request.args.get("path", ".")) 

    if not files.exists(path):
        return {
            "folders": [],
            "files": []
        }

    if not files.is_dir(path):
        return {
            "folders": [],
            "files": []
        }

    folders, _files = files.list_dir(path)

    return {
        "folders": folders,
        "files": _files
    }

@api.route("/admin/user/<user_id>/update", methods=["POST"])
@admin_route
def api_admin_user_update(user_id):
    admin = request.form.get("admin") == "on"

    db.session.execute(db.update(User).where(User.id == user_id).values(admin=admin))
    db.session.commit()

    return redirect(url_for("admin"))

@api.route("/admin/user/<user_id>/delete", methods=["POST"])
@admin_route
def api_admin_user_delete(user_id):
    db.session.execute(db.delete(User).where(User.id == user_id))
    db.session.commit()

    return redirect(url_for("admin"))