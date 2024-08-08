# MySQL_Advanced
In this project, we learned advanced statements and functionalities of MYSQL.

Topics Covered:
- How to create tables with constraints
- How to optimize queries by adding indexes
- What is and how to implement stored procedures and functions in MySQL
- What is and how to implement views in MySQL
- What is and how to implement triggers in MySQL

Table of Contents:
- [0. We are all unique!](#0-we-are-all-unique)
- [1. In and not out](#1-in-and-not-out)
- [2. Best band ever!](#2-best-band-ever)
- [3. Old school band](#3-old-school-band)
- [4. Buy buy buy](#4-buy-buy-buy)
- [5. Email validation to sent](#5-email-validation-to-sent)
- [6. Add bonus](#6-add-bonus)
- [7. Average score](#7-average-score)
- [8. Optimize simple search](#8-optimize-simple-search)
- [9. Optimize search and score](#9-optimize-search-and-score)
- [10. Safe divide](#10-safe-divide)

---
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
<sub>[Return to top](#mysql_advanced)</sub>

## 1. In and not out
Write a SQL script that creates a table `users` following these requirements:

- With these attributes:
    - `id`, integer, never null, auto increment and primary key
    - `email`, string (255 characters), never null and unique
    - `name`, string (255 characters)
    - `country`, enumeration of countries: `US`, `CO` and `TN`, never null (= default will be the first element of the enumeration, here `US`)
- If the table already exists, your script should not fail
- Your script can be executed on any database
- File: `1-country_users.sql`

```sh
$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
$ 
$ cat 1-country_users.sql | mysql -uroot -p holberton
Enter password: 
$ 
$ echo 'INSERT INTO users (email, name, country) VALUES ("bob@dylan.com", "Bob", "US");' | mysql -uroot -p holberton
Enter password: 
$ echo 'INSERT INTO users (email, name, country) VALUES ("sylvie@dylan.com", "Sylvie", "CO");' | mysql -uroot -p holberton
Enter password: 
$ echo 'INSERT INTO users (email, name, country) VALUES ("jean@dylan.com", "Jean", "FR");' | mysql -uroot -p holberton
Enter password: 
ERROR 1265 (01000) at line 1: Data truncated for column 'country' at row 1
$ 
$ echo 'INSERT INTO users (email, name) VALUES ("john@dylan.com", "John");' | mysql -uroot -p holberton
Enter password: 
$ 
$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
id  email   name    country
1   bob@dylan.com   Bob US
2   sylvie@dylan.com    Sylvie  CO
3   john@dylan.com  John    US
$ 
```
<sub>[Return to top](#mysql_advanced)</sub>

## 2. Best band ever!
Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

**Requirements:**

- Import this table dump: [metal_bands.sql](metal_bands.sql)
- Column names must be: `origin` and `nb_fans`
- Your script can be executed on any database
- File: `2-fans.sql`

**Context:** _Calculate/compute something is always power intensive… better to distribute the load!_

```sh
$ cat metal_bands.sql | mysql -uroot -p holberton
Enter password: 
$ 
$ cat 2-fans.sql | mysql -uroot -p holberton > tmp_res ; head tmp_res
Enter password: 
origin  nb_fans
USA 99349
Sweden  47169
Finland 32878
United Kingdom  32518
Germany 29486
Norway  22405
Canada  8874
The Netherlands 8819
Italy   7178
$ 
```
<sub>[Return to top](#mysql_advanced)</sub>

## 3. Old school band
Write a SQL script that lists all bands with `Glam rock` as their main style, ranked by their longevity

**Requirements:**

- Import this table dump: [metal_bands.sql](metal_bands.sql)
- Column names must be: `band_name` and `lifespan` (in years)
- You should use attributes `formed` and `split` for computing the `lifespan`
- Your script can be executed on any database
- File: `3-glam_rock.sql`

```sh
$ cat metal_bands.sql | mysql -uroot -p holberton
Enter password: 
$ 
$ cat 3-glam_rock.sql | mysql -uroot -p holberton 
Enter password: 
band_name   lifespan
Alice Cooper    56
Mötley Crüe   34
Marilyn Manson  31
The 69 Eyes 30
Hardcore Superstar  23
Nasty Idols 0
Hanoi Rocks 0
$ 
```
<sub>[Return to top](#mysql_advanced)</sub>

## 4. Buy buy buy
Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

Quantity in the table `items` can be negative.

- Given Files: [4-init.sql](4-init.sql), [4-main.sql](4-main.sql)
- File: `4-store.sql`

**Context:** _Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!_

```sh
$ cat 4-init.sql | mysql -uroot -p holberton 
Enter password: 
$ 
$ cat 4-store.sql | mysql -uroot -p holberton 
Enter password: 
$ 
$ cat 4-main.sql | mysql -uroot -p holberton 
Enter password: 
name    quantity
apple   10
pineapple   10
pear    10
--
--
name    quantity
apple   6
pineapple   10
pear    8
item_name   number
apple   1
apple   3
pear    2
$ 
```
<sub>[Return to top](#mysql_advanced)</sub>

## 5. Email validation to sent
Write a SQL script that creates a trigger that resets the attribute `valid_email` only when the `email` has been changed.

**Context:** _Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!_

- Given Files: [5-init.sql](5-init.sql), [5-main.sql](5-main.sql)
- File: `5-valid_email.sql`

```sh
$ cat 5-init.sql | mysql -uroot -p holberton 
Enter password: 
$ 
$ cat 5-valid_email.sql | mysql -uroot -p holberton 
Enter password: 
$ 
$ cat 5-main.sql | mysql -uroot -p holberton 
Enter password: 
id  email   name    valid_email
1   bob@dylan.com   Bob 0
2   sylvie@dylan.com    Sylvie  1
3   jeanne@dylan.com    Jeanne  1
--
--
id  email   name    valid_email
1   bob@dylan.com   Bob 1
2   sylvie+new@dylan.com    Sylvie  0
3   jeanne@dylan.com    Jannis  1
--
--
id  email   name    valid_email
1   bob@dylan.com   Bob 1
2   sylvie+new@dylan.com    Sylvie  0
3   jeanne@dylan.com    Jannis  1
$ 
```
<sub>[Return to top](#mysql_advanced)</sub>

## 6. Add bonus
Write a SQL script that creates a stored procedure `AddBonus` that adds a new correction for a student.

**Requirements:**

- Procedure `AddBonus` is taking 3 inputs (in this order):
    - `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing `users`)
    - `project_name`, a new or already exists `projects` \- if no `projects.name` found in the table, you should create it
    - `score`, the score value for the correction

**Context:** _Write code in SQL is a nice level up!_

- Given Files: [6-init.sql](6-init.sql), [6-main.sql](6-main.sql)
- File: `6-bonus.sql`

```sh
$ cat 6-init.sql | mysql -uroot -p holberton 
Enter password: 
$ 
$ cat 6-bonus.sql | mysql -uroot -p holberton 
Enter password: 
$ 
$ cat 6-main.sql
Enter password: 
$ 
$ cat 6-main.sql | mysql -uroot -p holberton 
Enter password: 
id  name
1   C is fun
2   Python is cool
user_id project_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
--
--
id  name
1   C is fun
2   Python is cool
3   Bonus project
4   New bonus
user_id project_id  score
1   1   80
1   2   96
2   1   91
2   2   73
2   2   100
2   3   100
1   3   10
2   4   90
$ 
```
<sub>[Return to top](#mysql_advanced)</sub>

## 7. Average score
Write a SQL script that creates a stored procedure `ComputeAverageScoreForUser` that computes and store the average score for a student. Note: An average score can be a decimal

**Requirements:**

- Procedure `ComputeAverageScoreForUser` is taking 1 input:
    - `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing `users`)
    - 
- Given Files: [7-init.sql](7-init.sql), [7-main.sql](7-main.sql)
- File: `7-average_score.sql`

```sh
$ cat 7-init.sql | mysql -uroot -p holberton 
Enter password: 
$ 
$ cat 7-average_score.sql | mysql -uroot -p holberton 
Enter password: 
$ 
$ cat 7-main.sql | mysql -uroot -p holberton 
Enter password: 
id  name    average_score
1   Bob 0
2   Jeanne  0
user_id project_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
--
--
id  name    average_score
1   Bob 0
2   Jeanne  82
$ 
```
<sub>[Return to top](#mysql_advanced)</sub>

## 8. Optimize simple search
Write a SQL script that creates an index `idx_name_first` on the table `names` and the first letter of `name`.

**Requirements:**

- Import this table dump: [names.sql.zip](https://intranet-projects-files.s3.amazonaws.com/holbertonschool-webstack/632/names.sql.zip "names.sql.zip")
- Only the first letter of `name` must be indexed

**Context:** _Index is not the solution for any performance issue, but well used, it’s really powerful!_

- File: `8-index_my_names.sql`

```sh
$ cat names.sql | mysql -uroot -p holberton
Enter password: 
$ 
$ mysql -uroot -p holberton
Enter password: 
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%';
+-------------+
| COUNT(name) |
+-------------+
|      302936 |
+-------------+
1 row in set (2.19 sec)
mysql> 
mysql> exit
bye
$ 
$ cat 8-index_my_names.sql | mysql -uroot -p holberton 
Enter password: 
$ 
$ mysql -uroot -p holberton
Enter password: 
mysql> SHOW index FROM names;
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non_unique | Key_name       | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| names |          1 | idx_name_first |            1 | name        | A         |          25 |        1 | NULL   | YES  | BTREE      |         |               |
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
1 row in set (0.00 sec)
mysql> 
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%';
+-------------+
| COUNT(name) |
+-------------+
|      302936 |
+-------------+
1 row in set (0.82 sec)
mysql> 
mysql> exit
bye
$ 
```
<sub>[Return to top](#mysql_advanced)</sub>

## 9. Optimize search and score
Write a SQL script that creates an index `idx_name_first_score` on the table `names` and the first letter of `name` and the `score`.

**Requirements:**

- Import this table dump: [names.sql.zip](https://intranet-projects-files.s3.amazonaws.com/holbertonschool-webstack/632/names.sql.zip "names.sql.zip")
- Only the first letter of `name` AND `score` must be indexed

- File: `9-index_name_score.sql`

```sh
$ cat names.sql | mysql -uroot -p holberton
Enter password: 
$ 
$ mysql -uroot -p holberton
Enter password: 
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%' AND score < 80;
+-------------+
| count(name) |
+-------------+
|       60717 |
+-------------+
1 row in set (2.40 sec)
mysql> 
mysql> exit
bye
$ 
$ cat 9-index_name_score.sql | mysql -uroot -p holberton 
Enter password: 
$ 
$ mysql -uroot -p holberton
Enter password: 
mysql> SHOW index FROM names;
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non_unique | Key_name             | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| names |          1 | idx_name_first_score |            1 | name        | A         |          25 |        1 | NULL   | YES  | BTREE      |         |               |
| names |          1 | idx_name_first_score |            2 | score       | A         |        3901 |     NULL | NULL   | YES  | BTREE      |         |               |
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
2 rows in set (0.00 sec)
mysql> 
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%' AND score < 80;
+-------------+
| COUNT(name) |
+-------------+
|       60717 |
+-------------+
1 row in set (0.48 sec)
mysql> 
mysql> exit
bye
$ 
```
<sub>[Return to top](#mysql_advanced)</sub>

## 10. Safe divide
Write a SQL script that creates a function `SafeDiv` that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

**Requirements:**

- You must create a function
- The function `SafeDiv` takes 2 arguments:
    - `a`, INT
    - `b`, INT
- And returns `a / b` or 0 if `b == 0`

- Given Files: [10-init.sql](10-init.sql)
- File: `10-div.sql`

```sh
$ cat 10-init.sql | mysql -uroot -p holberton
Enter password: 
$ 
$ cat 10-div.sql | mysql -uroot -p holberton
Enter password: 
$ 
$ echo "SELECT (a / b) FROM numbers;" | mysql -uroot -p holberton
Enter password: 
(a / b)
5.0000
0.8000
0.6667
2.0000
NULL
0.7500
$ 
$ echo "SELECT SafeDiv(a, b) FROM numbers;" | mysql -uroot -p holberton
Enter password: 
SafeDiv(a, b)
5
0.800000011920929
0.6666666865348816
2
0
0.75
$ 
```
<sub>[Return to top](#mysql_advanced)</sub>
