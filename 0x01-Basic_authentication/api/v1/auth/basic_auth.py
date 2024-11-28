#!/usr/bin/env python3
"""This is basic of basics
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ This wasnt documented
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """This for checkigner euth auth
        """
        if authorization_header is None or\
                not isinstance(authorization_header, str):
            print("first")
            return None
        auth_word = authorization_header.split()
        if len(auth_word) != 2 or auth_word['0'] != 'Basic':
            print("secodn")
            return None
        return auth_word[1]
