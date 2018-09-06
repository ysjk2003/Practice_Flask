# -*- coding: utf-8 -*-

from flask import Flask, url_for
app = Flask(__name__)

@app.route('/hello/')
def hello():
    return 'Hello Flask!'

@app.route('/proflie/<username>')   #<username>이 변수, 해당 변수는 URI와 일치하는 뷰 함수의 인자로 사용할 수 있다
def get_proflie(username):          #127.0.0.1:5000/profile/username으로 접속하면 profile: username 출력
    return 'proflie : ' + username  #URI의 끝점을 endpoint라고 함, 여기서는 username이 endpoint

if __name__ == '__main__':          #<int:age>같은 형태로 변수의 타입을 지정해 줄 수 도 있다. 기본값은 str
                                    #int이외의 다른 변환기는 float와 문자열을 변환하지만 마지막에 /를 포함하는 path와 UUID가 있다
    with app.test_request_context():#test_request_context()는 flask에서 제공하는 HTTP요청을 테스트 할 수 있는 함수
        print (url_for('hello'))      #url_for는 함수명으로 URI를 얻을 수 있다
        print (url_for('get_proflie', username='flask'))
#url_for()함수의 첫번째 인자로 함수명을 넘겨주고 두 번째 인자로 URI로 전달되는 값들을 넘겨주면 해당 함수를 호출할 수 있는 URI로 반환

'''URI(/hello/)는 endpoint가 /로 끝난다. 파일 시스템의 폴더와 유사하다
/가 없는 URI를 요청하더라도 /가 있는 URI로 리디렉션(/를 붙여 새로고침한다고 생각하면 될 듯 하다) 된다.
URI(/profile/flask)는 endpoint가 /로 끝나지 않는 경우로 파일 시스템의 파일과 같다.
URI(/profile/flask/)를 요청하면 해당 URI를 찾지 못한다
때문에 /가 있을 때와 없을 때의 의미를 명확하게 구분할 수 있어야 한다.'''