#!/usr/bin/env python3
""" This is for Auth
"""
from flask import request
from typing import List, TypeVar
from models.user import User


user = TypeVar('User')


class Auth:
    """ THis nuts
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return False

    def authorization_header(self, request=None) -> str:
        return None

    def current_user(self, request=None) -> user:
        return None
