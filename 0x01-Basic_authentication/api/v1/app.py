#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import Basic_Auth
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
excluded = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']

AUTH_TYPE = os.getenv('AUTH_TYPE')
if AUTH_TYPE == 'Basic_Auth':
    auth = Basic_Auth()
elif AUTH_TYPE == 'Auth':
    auth = Auth()


@app.before_request
def before_req():
    """ THs is nym mss
    """
    if auth is None:
        pass
    elif not auth.require_auth(request.path, excluded):
        pass
    elif auth.authorization_header(request) is None:
        abort(401)
    elif auth.current_user(request) is None:
        abort(403)


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized error
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(403)
def forbedden(err) -> str:
    """ You may just close it
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
