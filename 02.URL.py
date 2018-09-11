#-*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route('/hello')  #127.0.0.1:5000/hello의 경로로 들어가면 바로 밑의 함수가 실행됨
def hello():
    return 'Hello Flask!'

if __name__ == '__main__':
    app.run()