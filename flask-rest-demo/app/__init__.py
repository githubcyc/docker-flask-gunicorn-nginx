
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
from flask import got_request_exception
from app.errors import custom_api_error_handler
from flask_restful import Api
from app.resources.hello import HelloWorld

def create_app(config_name='default'):
    app = Flask(__name__)
    got_request_exception.connect(custom_api_error_handler, sender=app)
    api = Api(app)
    @app.errorhandler(Exception)
    def api_error_handler(exception, **kwargs):
        payload = {
            'type': 'InternalServerError',
            'description': 'Internal Error',
            # 'url': request.url
            }
        if isinstance(exception, HTTPException):
            payload['type'] = 'HTTPException'
            payload['description'] = exception.description
            payload['code'] = exception.code
            status_code = exception.code
        else:
            payload['description'] = exception.args
            payload['code'] = 500
            status_code = 500
        return jsonify(payload), status_code
    api.add_resource(HelloWorld, '/')
    return app