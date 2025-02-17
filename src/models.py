from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    password_reset = db.Column(db.Boolean())

    def set_password(self, password):
        self.password_hash = password #generate_password_hash(password)

    def check_password(self, password):
        return  self.password_hash == password #check_password_hash(self.password_hash, password)