from flask import Flask
from controllers.seed.seed_controller import seed_controller

app = Flask(__name__)

app.register_blueprint(seed_controller, url_prefix='/seed')