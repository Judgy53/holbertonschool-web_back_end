# personal_data
In this project, we learned how to obfuscate PII fields, encrypt a password and authenticate to a database in Python.

Covered topics :
- Examples of Personally Identifiable Information (PII)
- How to implement a log filter that will obfuscate PII fields
- How to encrypt a password and check the validity of an input password
- How to authenticate to a database using environment variables

---
Table of contents:
- [0. Regex-ing](#0-regex-ing)
- [1. Log formatter](#1-log-formatter)

## 0. Regex-ing
Write a function called `filter_datum` that returns the log message obfuscated:

- Arguments:
    - `fields`: a list of strings representing all fields to obfuscate
    - `redaction`: a string representing by what the field will be obfuscated
    - `message`: a string representing the log line
    - `separator`: a string representing by which character is separating all fields in the log line (`message`)
- The function should use a regex to replace occurrences of certain field values.
- `filter_datum` should be less than 5 lines long and use `re.sub` to perform the substitution with a single regex.
- File: `filtered_logger.py`

---

Given Files:
- [0-main.py](0-main.py)

Expected Output:
```sh
$ ./0-main.py
name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;
name=bob;email=bob@dylan.com;password=xxx;date_of_birth=xxx;
```

## 1. Log formatter
Copy the following code into `filtered_logger.py`.

```py
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError
```

- Update the class to accept a list of strings `fields` constructor argument.
- Implement the `format` method to filter values in incoming log records using `filter_datum`. Values for fields in `fields` should be filtered.
- DO NOT extrapolate `FORMAT` manually. The `format` method should be less than 5 lines long.
- File: `filtered_logger.py`

---
Given Files:
- [1-main.py](1-main.py)

Expected output:
```sh
$ ./main.py
[HOLBERTON] my_logger INFO 2019-11-19 18:24:25,105: name=Bob;email=***;ssn=***;password=***;
```