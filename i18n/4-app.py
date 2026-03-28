#!/usr/bin/env python3
"""
Force locale with URL parameter
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Configuration class for Babel
    """
    LANGUAGES =["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


def get_locale() -> str:
    """
    Determine the best match with our supported languages.
    Checks for 'locale' parameter in URL.
    """
    # Check if 'locale' parameter is in the URL
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    
    # Default behavior if parameter is not present or not supported
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel()
babel.init_app(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders a parametrized html template
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)