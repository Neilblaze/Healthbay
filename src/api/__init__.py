import os
from flask import Flask

from .models import db

app = Flask(__name__)

from .middleware.firebase_auth import Middleware

app.wsgi_app = Middleware(app.wsgi_app)
# app.config.from_object(os.environ["APP_SETTINGS"])
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)  # for initializing refactored cyclic imports

from .routes import api

app.register_blueprint(api, url_prefix="/")
