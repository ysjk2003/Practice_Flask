# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route('/')
def index():
    resp = make_response(render_template('hello.html')) #make_response함수로 헤더정보를 추가하거나 response객체를 수정해야 할 수 있다
    resp.set_cookie('username','flask')           #쿠키생성. username이 키, flask가 값
    return resp

if __name__ == '__main__':
    app.run()