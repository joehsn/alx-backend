#!/usr/bin/env python3
"""
0. Basic Flask app task's module.
"""""
from flask import Flask, render_template

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/')
def get_index():
    """
    Base route.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
