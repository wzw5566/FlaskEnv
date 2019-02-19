from flask import Blueprint

home_blue = Blueprint('home_blue', __name__)

def init_home_blue(app):
    app.register_blueprint(blueprint=home_blue)

@home_blue.route('/')
def home():
    return 'Flask Home'