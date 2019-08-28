# ===============================================================
# Author: Rodolfo Ferro
# Email: ferro@cimat.mx
# Twitter: @FerroRodolfo
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro,
# for his workshop at RIIAA 2.0. Any explicit usage of
# this script or its contents is granted according to
# the license provided and its conditions.
# ===============================================================

# -*- coding: utf-8 -*-

from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def url_principal():
    return "<h1>Hello world!</h1>"


@app.route('/<int:lucky_number>')
def luck_url(lucky_number):
    response = {
        "Status code": 200,
        "Lucky number": lucky_number
    }
    
    return jsonify(response)

    
@app.route('/<string:name>')
def url_name(name):
    html_code = f"""
    <h1>Hello, {name}!
    <p>Welcome to the matrix.</p>
    """
    return html_code


if __name__ == '__main__':
    app.run(debug=True, port=5000)