from app.ext import db


class Persion(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    p_name = db.Column(db.String(16))
    p_age = db.Column(db.Integer, default=18)

