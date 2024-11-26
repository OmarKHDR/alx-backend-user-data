#!/usr/bin/env python3
'''
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which
'''
import re
from typing import List, Any


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    '''Heloo wthern f mdf d'''
    pattern: str = '|'.join([f'(?<={st}=).*?(?={separator})' for st in fields])
    return re.sub(pattern, redaction, message)
