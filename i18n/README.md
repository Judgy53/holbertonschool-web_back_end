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