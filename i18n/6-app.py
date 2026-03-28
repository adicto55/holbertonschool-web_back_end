#!/usr/bin/env python3
"""
6-app.py
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

class Config:
    """Config class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

# Simulated users
users = {
    1: {"name": "Balou", "locale": "fr"},
    2: {"name": "Beyonce", "locale": "en"},
    3: {"name": "Spock", "locale": "kg"},  # unsupported
    4: {"name": "Teletubby", "locale": None},
}


def get_user():
    """Retrieve a user based on login_as parameter"""
    user_id = request.args.get("login_as")
    if user_id:
        try:
            return users.get(int(user_id))
        except Exception:
            return None
    return None


@app.before_request
def before_request():
    """Set user globally before each request"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages"""

    # 1. Locale from URL parameters
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale

    # 2. Locale from user settings
    if g.get("user"):
        user_locale = g.user.get("locale")
        if user_locale and user_locale in app.config["LANGUAGES"]:
            return user_locale

    # 3. Locale from request header
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """Render index page"""
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(debug=True)