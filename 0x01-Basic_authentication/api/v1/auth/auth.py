#!/usr/bin/env python3
""" This is for Auth
"""
from flask import request
from typing import List, TypeVar
import re
# from models.user import User


user = TypeVar('User')


class Auth:
    """ THis is an auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ THis is an auth class
        """
        if (path is None) or (excluded_paths is None):
            return True
        exc_pathes = map(lambda st: st.strip('/'), excluded_paths)
        myPath = path.strip('/')
        if myPath in exc_pathes:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ THis is an auth class
        """
        if request is None or not request.headers.get('Authorization'):
            return None
        else:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> user:
        """ THis is an auth class
        """
        return None
