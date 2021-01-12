from flask import Blueprint

seed_controller = Blueprint('seed_controller', __name__)

@seed_controller.route('/generate')
def generate():
    return "This is an example app"

@seed_controller.route('/validate')
def validate():
    return "This is an example app"