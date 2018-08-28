# -*- coding: utf-8 -*-

from flask import Flask, url_for
app = Flask(__name__)

@app.route('/hello/')
def hello():
    return 'Hello Flask!'

@app.route('/proflie/<username>')  #<username>이 변수, 해당 변수는 URI와 일치하는 뷰 함수의 인자로 사용할 수 있다
def get_proflie(username):         #127.0.0.1:5000/profile/username으로 접속하면 profile: username 출력
    return 'proflie : ' + username #URI의 끝점을 endpoint라고 함, 여기서는 username이 endpoint

if __name__ == '__main__':         #<int:age>같은 형태로 변수의 타입을 지정해 줄 수 도 있다. 기본값은 str
    app.run()                      #int이외의 다른 변환기는 float와 문자열을 변환하지만 마지막에 /를 포함하는 path가 있다
    with app.test_request_context():
        print url_for('hello')
        print url_for('get_proflie', username='flask')