#!/usr/bin/env python3
"""This is basic of basics
"""
from api.v1.auth.auth import Auth
import base64
from typing import Tuple, TypeVar


U = TypeVar('User')

class BasicAuth(Auth):
    """ This wasnt documented
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """This for checkigner euth auth
        """
        if authorization_header is None or\
                not isinstance(authorization_header, str):
            return None
        auth_word = authorization_header.split()
        if len(auth_word) != 2 or auth_word[0] != 'Basic':
            return None
        return authorization_header.strip("Basic ")

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ THis is for some decode
        """
        if base64_authorization_header is None or\
                not isinstance(base64_authorization_header, str):
            return None
        try:
            code = base64.b64decode(base64_authorization_header)
            return code.decode()
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """ Forgot it tehehe
        """
        if decoded_base64_authorization_header is None or\
                not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        arr = decoded_base64_authorization_header.split(':')
        if len(arr) == 1:
            return (None, None)
        else:
            return (arr[0], ':'.join(arr[1:]))

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> U:
        """ This is prefinal
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
