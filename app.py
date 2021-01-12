from flask import Flask
from controllers.seed import seed_controller;

app = Flask(__name__)

app.register_blueprint(seed_controller, url_prefix='/seed')