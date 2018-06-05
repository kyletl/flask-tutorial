import os

from flask import Flask, current_app


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        # Load instance config when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load test config
        app.config.from_mapping(test_config)

    # ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello():
        return 'Hello, World!'

    # initialize the db
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app


if __name__ == "__main__":
    app = current_app or create_app()
    app.run(host='0.0.0.0', port=80)
