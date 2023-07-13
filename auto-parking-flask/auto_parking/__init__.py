import os

from flask import Flask, url_for, redirect, render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
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
    
    @app.route("/favicon.ico")
    def favicon():
        return redirect(url_for("static", filename="favicon.ico"))
    
    @app.errorhandler(404)
    def not_found(e):
        return render_template("notfound.html")
    
    @app.route("/")
    def parking_index():
        return redirect("/parking/")
    
    from .controller import auth
    app.register_blueprint(auth.blue_print)

    from .controller import parking
    app.register_blueprint(parking.blue_print)

    from .controller import summary
    app.register_blueprint(summary.blue_print)


    return app
