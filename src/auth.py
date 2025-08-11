from flask import flash, session, redirect, url_for, request
from src.models import db, User

def is_logged():
    return bool(session.get("user"))

def get_user():
    return db.session.execute(db.select(User).where(User.id == session["user"]["id"])).scalar_one_or_none()

def auth_route(func, admin=False):
    def wrapper(*args, **kwargs):
        if not is_logged():
            return redirect(url_for("login", next=request.path))
        
        if admin and not get_user().admin:
            flash("You don't have permission to access this page.", "danger")
            return redirect(url_for("index"))

        return func(*args, **kwargs)
    
    wrapper.__name__ = func.__name__ 
    return wrapper

def logged_route(func):
    return auth_route(func, admin=False)

def admin_route(func):
    return auth_route(func, admin=True)

def set_user_session(user):
    session["user"] = {
        "id": user.id
    }