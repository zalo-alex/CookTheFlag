from flask import session, redirect, url_for, request

def is_logged():
    return bool(session.get("user"))

def auth_route(func):
    def wrapper(*args, **kwargs):
        if not is_logged():
            return redirect(url_for("login", next=request.path))
        
        return func(*args, **kwargs)
    
    wrapper.__name__ = func.__name__ 
    return wrapper

def set_user_session(user):
    session["user"] = {
        "username": user.username
    }