# project/server/__init__.py
import os

#import boto3
from flask import Flask, render_template
#from flask_security import Security, SQLAlchemyUserDatastore
#from flask_bcrypt import Bcrypt
#from flask_debugtoolbar import DebugToolbarExtension
#from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
#from flask_uploads import UploadSet, configure_uploads, patch_request_class, IMAGES

class BaseConfig(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///toy_share.sqlite'

config = BaseConfig()

# instantiate the extensions
#bcrypt = Bcrypt()
#toolbar = DebugToolbarExtension()
#bootstrap = Bootstrap()
db = SQLAlchemy()
#migrate = Migrate()
#security = Security()
#photos = UploadSet('photos', IMAGES)
#s3 = boto3.client("s3")  # even without credentials this should work


def create_app(script_info=None):

    from logging.config import dictConfig

    # Set up logging at DEBUG level ...
    # From here: http://flask.pocoo.org/docs/dev/logging/
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'DEBUG',
            'handlers': ['wsgi']
        }
    })

    # instantiate the app
    app = Flask(__name__)

    # set config
    app.config.from_object(config)

    # set up extensions
    #bcrypt.init_app(app)
    #toolbar.init_app(app)
    #bootstrap.init_app(app)
    db.init_app(app)
    #migrate.init_app(app, db)

    # register blueprints
    #from .views import toys_blueprint
    #app.register_blueprint(toys_blueprint)
    
    # flask security
    #from coffeeshop.server.models import User, Role
    #from coffeeshop.server.user.forms import ExtendedRegisterForm
    #datastore = SQLAlchemyUserDatastore(db, User, Role)
    #security_ctx = security.init_app(
    #    app,
    #    datastore,
    #    register_form=ExtendedRegisterForm  # extend the register
    #)

    # error handlers
    @app.errorhandler(401)
    def unauthorized_page(error):
        return render_template("errors/401.html"), 401

    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template("errors/403.html"), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template("errors/500.html"), 500

    # shell context for flask cli
    #@app.shell_context_processor
    #def ctx():
    #    return {"app": app, "db": db}

    # flask-uploads
    #configure_uploads(app, (photos, ))
    #patch_request_class(app, None)

    # GNU Terry Pratchett
    #@app.after_request
    #def gnu_terry_pratchett(resp):
    #    resp.headers.add("X-Clacks-Overhead", "GNU Terry Pratchett")
    #    return resp

    return app

