import sys
import os
import logging

from flask import Flask
from flask_cors import CORS

sys.path.append(os.path.dirname(os.path.realpath(__file__)))


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    logging.getLogger('flask_cors').level = logging.DEBUG


    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'dartview.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    import dartview
    import sortdata
    
    app.register_blueprint(dartview.bp)
    app.register_blueprint(sortdata.bp)
    
    return app

    