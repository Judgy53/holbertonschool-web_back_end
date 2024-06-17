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

## 0. Regex-ing
Write a function called `filter_datum` that returns the log message obfuscated:

- Arguments:
    - `fields`: a list of strings representing all fields to obfuscate
    - `redaction`: a string representing by what the field will be obfuscated
    - `message`: a string representing the log line
    - `separator`: a string representing by which character is separating all fields in the log line (`message`)
- The function should use a regex to replace occurrences of certain field values.
- `filter_datum` should be less than 5 lines long and use `re.sub` to perform the substitution with a single regex.

---

Given Files:
- [0-main.py](0-main.py)

Expected Output:
```sh
$ ./0-main.py
name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;
name=bob;email=bob@dylan.com;password=xxx;date_of_birth=xxx;
```

**Repo:**

- GitHub repository: `holbertonschool-web_back_end`
- Directory: `personal_data`
- File: `filtered_logger.py`