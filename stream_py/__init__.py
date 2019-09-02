from .sources import ScreenSource

from flask import Flask, Response, render_template


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    source = ScreenSource()

    if not config:
        app.config.from_object("configs")
    else:
        app.config.from_mapping(config)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/source/")
    def stream_source():
        return Response(source, mimetype='multipart/x-mixed-replace; boundary=frame')

    return app
