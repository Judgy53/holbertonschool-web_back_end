#!/usr/bin/env python3
"""
Module that defines multiple classes and function to filter log inputs.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Obfuscate fields value in a log message."""
    replacement: str = rf'\1{redaction}{separator}'
    for f in fields:
        message = re.sub(rf'({f}=).*?{separator}', replacement, message)
    return message
