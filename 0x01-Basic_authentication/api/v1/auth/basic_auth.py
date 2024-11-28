#!/usr/bin/env python3
"""This is basic of basics
"""
from api.v1.auth.auth import Auth
import base64


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
