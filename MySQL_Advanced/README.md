# MySQL_Advanced
In this project, we learned advanced statements and functionalities of MYSQL.

Topics Covered:
- How to create tables with constraints
- How to optimize queries by adding indexes
- What is and how to implement stored procedures and functions in MySQL
- What is and how to implement views in MySQL
- What is and how to implement triggers in MySQL


## 0. We are all unique!
Write a SQL script that creates a table `users` following these requirements:

- With these attributes:
    - `id`, integer, never null, auto increment and primary key
    - `email`, string (255 characters), never null and unique
    - `name`, string (255 characters)
- If the table already exists, your script should not fail
- Your script can be executed on any database
- File: `0-uniq_users.sql`

**Context:** _Making an attribute unique directly in the table schema will enforce your business rules and avoid bugs in your application_

```sh
$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
$ 
$ cat 0-uniq_users.sql | mysql -uroot -p holberton
Enter password: 
$ 
$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");' | mysql -uroot -p holberton
Enter password: 
$ echo 'INSERT INTO users (email, name) VALUES ("sylvie@dylan.com", "Sylvie");' | mysql -uroot -p holberton
Enter password: 
$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Jean");' | mysql -uroot -p holberton
Enter password: 
ERROR 1062 (23000) at line 1: Duplicate entry 'bob@dylan.com' for key 'email'
$ 
$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
id  email   name
1   bob@dylan.com   Bob
2   sylvie@dylan.com    Sylvie
$ 
```
