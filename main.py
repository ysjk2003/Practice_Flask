#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import *
import sqlite3, hashlib, uuid, re, ast, time, os, operator, shutil

app = Flask(__name__)

@app.route("/")
@app.route("/main.html")
def hello():
    return render_template('main.html')

@app.route("/login.html")
@app.route("/login",methods=["GET,POST"])
def login():
    if request.methods == "GET":
        return render_template("login.html",s_username=None)

if __name__ == "__main__":
    app.run(debug=True)