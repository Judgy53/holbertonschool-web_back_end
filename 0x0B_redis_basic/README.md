# redis_basic
In this project, we learned how to use redis in python.

Covered topics:
- Learn how to use redis for basic operations
- Learn how to use redis as a simple cache

Table of Contents:
- [0. Writing strings to Redis](#0-writing-strings-to-redis)
- [1. Reading from Redis and recovering original type](#1-reading-from-redis-and-recovering-original-type)

## 0. Writing strings to Redis
Create a `Cache` class. In the `__init__` method, store an instance of the Redis client as a private variable named `_redis` (using `redis.Redis()`) and flush the instance using `flushdb`.

Create a `store` method that takes a `data` argument and returns a string. The method should generate a random key (e.g. using `uuid`), store the input data in Redis using the random key and return the key.

Type-annotate `store` correctly. Remember that `data` can be a `str`, `bytes`, `int` or `float`.

- Given File: [0-main.py](0-main.py)
- Out File: `exercise.py`

```sh
$ python3 0-main.py 
3a3e8231-b2f6-450d-8b0e-0f38f16e8ca2
b'hello'
$ 
```

## 1. Reading from Redis and recovering original type
Redis only allows to store string, bytes and numbers (and lists thereof). Whatever you store as single elements, it will be returned as a byte string. Hence if you store `"a"` as a UTF-8 string, it will be returned as `b"a"` when retrieved from the server.

In this exercise we will create a `get` method that take a `key` string argument and an optional `Callable` argument named `fn`. This callable will be used to convert the data back to the desired format.

Remember to conserve the original `Redis.get` behavior if the key does not exist.

Also, implement 2 new methods: `get_str` and `get_int` that will automatically parametrize `Cache.get` with the correct conversion function.

- Given File: [1-main.py](1-main.py)
- Out File: `exercise.py`

```
$ python3 1-main.py 
$ 
```