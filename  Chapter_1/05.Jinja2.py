# -*- coding: utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):   #/hello뒤에 아무것도 오지 않으면 None이 표시된다. (아마도 기본값 지정인듯 하다)
    return render_template('hello.html', name=name)  #hello.html파일에 있는 {{ name }}에 name을 대입한다.

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)  #app.run()에 옵션을 줄 수 있다
    #debug옵션은 파일에 수정이 가해지면 자동으로 서버를 재실행 시킨다. 기본값 flase
    #host는 접속주소를 의미하는것 같다. 기본값 127.0.0.1
    #port는 말 그대로 포트를 지정해 준다. 기본값 5000