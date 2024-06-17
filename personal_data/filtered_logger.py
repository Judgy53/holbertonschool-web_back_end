#!/usr/bin/env python3
"""
Module that defines multiple classes and function to filter log inputs.
"""

import re
import logging
import mysql.connector
import os
from typing import List


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def get_logger() -> logging.Logger:
    """Create a user_data logger that obfuscates PII fields"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(streamHandler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Create a mysql database connection using environment variables."""
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    name = os.getenv('PERSONAL_DATA_DB_NAME')
    return mysql.connector.connect(user=username, password=password,
                                   host=host, database=name)


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
        """Initialize the formatter with a list of fields to obfuscate"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.__fields__ = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format the specified record as text
        and obfuscate the necessary fields."""
        formatted: str = super().format(record)
        return filter_datum(self.__fields__, self.REDACTION,
                            formatted, self.SEPARATOR)
