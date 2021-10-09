from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/api/v1/hello-world-11')
    def index():
        return 'Hello world'

    return app



