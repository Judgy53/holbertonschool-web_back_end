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