#!/usr/bin/env python3
"""
5. Mock logging in task module.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},

}

class Config:
    """
    Config class to set available languages and other settings.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determine the best match for supported languages.
    """
    user = getattr(g, 'user', None)
    if user and user.get('locale') in app.config['LANGUAGES']:
        return user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """
    Retrieve user based on 'login_as' parameter.
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """
    Set the user in the global context.
    """
    g.user = get_user()


@app.route('/')
def index():
    """
    Render the index page.
    """
    return render_template('5-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
