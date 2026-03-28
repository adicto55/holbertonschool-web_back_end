#!/usr/bin/env python3
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)

class Config:
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
    user_id = request.args.get("login_as")
    if user_id:
        try:
            return users.get(int(user_id))
        except Exception:
            return None
    return None


@app.before_request
def before_request():
    g.user = get_user()


def get_locale():
    """Determine best locale"""

    # 1. URL param
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale

    # 2. User locale
    if g.get("user"):
        user_locale = g.user.get("locale")
        if user_locale and user_locale in app.config["LANGUAGES"]:
            return user_locale

    # 3. Header
    return request.accept_languages.best_match(app.config["LANGUAGES"])


# 🔥 IMPORTANT CHANGE HERE
babel = Babel(app, locale_selector=get_locale)


@app.route("/")
def index():
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(debug=True)