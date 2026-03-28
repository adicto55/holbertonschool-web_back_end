#!/usr/bin/env python3
"""
Mock logging in
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


class Config:
    """
    Configuration class for Babel
    """
    LANGUAGES =["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

# Mock database user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    Returns a user dictionary or None if the ID cannot be found
    or if login_as was not passed.
    """
    login_id = request.args.get('login_as')
    if login_id:
        try:
            return users.get(int(login_id))
        except ValueError:
            return None
    return None


@app.before_request
def before_request() -> None:
    """
    Find a user if any, and set it as a global on flask.g.user
    """
    g.user = get_user()


def get_locale() -> str:
    """
    Determine the best match with our supported languages.
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel()
babel.init_app(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders a parametrized html template
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)