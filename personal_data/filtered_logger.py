#!/usr/bin/env python3
"""
Module that defines multiple classes and function to filter log inputs.
"""

import re
import logging
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Obfuscate fields value in a log message."""
    replacement: str = rf'\1{redaction}{separator}'
    for f in fields:
        message = re.sub(rf'({f}=).*?{separator}', replacement, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.__fields__ = fields

    def format(self, record: logging.LogRecord) -> str:
        formatted: str = super().format(record)
        return filter_datum(self.__fields__, self.REDACTION,
                            formatted, self.SEPARATOR)
