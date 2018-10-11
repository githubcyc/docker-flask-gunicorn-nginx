
from werkzeug.exceptions import HTTPException
from flask import jsonify, request


def custom_api_error_handler(app, exception, **kwargs):
  payload = {
    'type': 'InternalServerError',
    'description': 'Internal Error',
    # 'method': request.method,
    'url': request.url
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
  print(payload)
  return payload, status_code