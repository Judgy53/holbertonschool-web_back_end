# i18n

In this project, we learned how to implement i18n in a Flask application using Flask-Babel

Covered Topics:
- Learn how to parametrize Flask templates to display different languages
- Learn how to infer the correct locale based on URL parameters, user settings or request headers
- Learn how to localize timestamps

---
Table of Contents:
- [0. Basic Flask app](#0-basic-flask-app)
- [1. Basic Babel setup](#1-basic-babel-setup)
- [2. Get locale from request](#2-get-locale-from-request)
- [3. Parametrize templates](#3-parametrize-templates)
  - [4. Force locale with URL parameter](#4-force-locale-with-url-parameter)

## 0. Basic Flask app
First you will setup a basic Flask app in `0-app.py`. Create a single `/` route and an `index.html` template that simply outputs “Welcome to Holberton” as page title (`<title>`) and “Hello world” as header (`<h1>`).

---
- Out File: `0-app.py, templates/0-index.html`

## 1. Basic Babel setup
Install the Babel Flask extension:

```sh
$ pip3 install flask_babel
```

Then instantiate the `Babel` object in your app. Store it in a module-level variable named `babel`.

In order to configure available languages in our app, you will create a `Config` class that has a `LANGUAGES` class attribute equal to `["en", "fr"]`.

Use `Config` to set Babel’s default locale (`"en"`) and timezone (`"UTC"`).

Use that class as config for your Flask app.

---
- Out File: `1-app.py, templates/1-index.html`

## 2. Get locale from request
Create a `get_locale` function with the `babel.localeselector` decorator. Use `request.accept_languages` to determine the best match with our supported languages.

---
- Out File: `2-app.py, templates/2-index.html`

## 3. Parametrize templates
Use the `_` or `gettext` function to parametrize your templates. Use the message IDs `home_title` and `home_header`.

Create a `babel.cfg` file containing

```conf
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```

Then initialize your translations with

```sh
$ pybabel extract -F babel.cfg -o messages.pot .
```

and your two dictionaries with

```sh
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
```

Then edit files `translations/[en|fr]/LC_MESSAGES/messages.po` to provide the correct value for each message ID for each language. Use the following translations:

| msgid | English | French |
| --- | --- | --- |
| `home_title` | `"Welcome to Holberton"` | `"Bienvenue chez Holberton"` |
| `home_header` | `"Hello world!"` | `"Bonjour monde!"` |

Then compile your dictionaries with

```sh
$ pybabel compile -d translations
```

Reload the home page of your app and make sure that the correct messages show up.

---
- Out File: `3-app.py, babel.cfg, templates/3-index.html, translations/en/LC_MESSAGES/messages.po, translations/fr/LC_MESSAGES/messages.po, translations/en/LC_MESSAGES/messages.mo, translations/fr/LC_MESSAGES/messages.mo`

### 4\. Force locale with URL parameter

mandatory

In this task, you will implement a way to force a particular locale by passing the `locale=fr` parameter to your app’s URLs.

In your `get_locale` function, detect if the incoming request contains `locale` argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.

Now you should be able to test different translations by visiting `http://127.0.0.1:5000?locale=[fr|en]`.

**Visiting `http://127.0.0.1:5000/?locale=fr` should display this level 1 heading:** 

![](previews/4.png)

---
- Out File: `4-app.py, templates/4-index.html`