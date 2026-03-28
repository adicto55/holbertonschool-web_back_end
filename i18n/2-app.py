#!/usr/bin/env python3
"""
Get locale from request
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Configuration class for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


def get_locale() -> str:
    """
    Determine the best match with our supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# Instantiate the Babel object and initialize it with the app and locale_selector
babel = Babel()
babel.init_app(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders a basic html template
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)