# user_authentication_service
In the industry, you should not implement your own authentication system and use a module or framework that doing it for you (like in Python-Flask: [Flask-User](https://flask-user.readthedocs.io/en/latest/)). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

Table of Contents:
- [0. User model](#0-user-model)
- [1. create user](#1-create-user)
- [2. Find user](#2-find-user)
- [3. update user](#3-update-user)
- [4. Hash password](#4-hash-password)

## 0. User model
In this task you will create a SQLAlchemy model named `User` for a database table named `users` (by using the [mapping declaration](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#declare-a-mapping "mapping declaration") of SQLAlchemy).

The model will have the following attributes:
- `id`, the integer primary key
- `email`, a non-nullable string
- `hashed_password`, a non-nullable string
- `session_id`, a nullable string
- `reset_token`, a nullable string

---
- Out File: `user.py`
- Given files: [0-main.py](0-main.py)
```py
$ python3 0-main.py
users
users.id: INTEGER
users.email: VARCHAR(250)
users.hashed_password: VARCHAR(250)
users.session_id: VARCHAR(250)
users.reset_token: VARCHAR(250)
```

## 1. create user
In this task, you will complete the `DB` class provided below to implement the `add_user` method.

```py
#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session
```

Note that `DB._session` is a private property and hence should NEVER be used from outside the `DB` class.

Implement the `add_user` method, which has two required string arguments: `email` and `hashed_password`, and returns a `User` object. The method should save the user to the database. No validations are required at this stage.

---
- Out file: `db.py`
- Given File: [1-main.py](1-main.py)
```sh
$ python3 1-main.py
1
2
```

## 2. Find user
In this task you will implement the `DB.find_user_by` method. This method takes in arbitrary keyword arguments and returns the first row found in the `users` table as filtered by the method’s input arguments. No validation of input arguments required at this point.

Make sure that SQLAlchemy’s `NoResultFound` and `InvalidRequestError` are raised when no results are found, or when wrong query arguments are passed, respectively.

**Warning:**
- `NoResultFound` has been moved from `sqlalchemy.orm.exc` to `sqlalchemy.exc` between the version 1.3.x and 1.4.x of SQLAchemy - please make sure you are importing it from `sqlalchemy.orm.exc`

---
- Out File: `db.py`
- Given File: [2-main.py](2-main.py) 
```sh
$ python3 2-main.py
1
1
Not found
Invalid
```

## 3. update user
In this task, you will implement the `DB.update_user` method that takes as argument a required `user_id` integer and arbitrary keyword arguments, and returns `None`.

The method will use `find_user_by` to locate the user to update, then will update the user’s attributes as passed in the method’s arguments then commit changes to the database.

If an argument that does not correspond to a user attribute is passed, raise a `ValueError`.

---
- Out File: `db.py`
- Given File: [3-main.py](3-main.py) 
```sh
$ python3 3-main.py
1
Password updated
```

## 4. Hash password
In this task you will define a `_hash_password` method that takes in a `password` string arguments and returns bytes.

The returned bytes is a salted hash of the input password, hashed with `bcrypt.hashpw`.

---
- Out File: `auth.py`
- Given File: [4-main.py](4-main.py) 
```sh
$ python3 4-main.py
b'$2b$12$eUDdeuBtrD41c8dXvzh95ehsWYCCAi4VH1JbESzgbgZT.eMMzi.G2'
```