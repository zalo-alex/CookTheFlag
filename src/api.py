from flask import Blueprint, request

from src.files import Files
from src.auth import auth_route

files = Files()

api = Blueprint("api", __name__, url_prefix="/api")

@api.route("/files")
@auth_route
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