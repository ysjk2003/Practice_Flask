# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def test():
    return render_template('post.html')  #templates폴더속 post.html을 가져옴

@app.route('/post', methods=['POST','GET'])  #methods=['POST']는 메소드를 POST형식으로 선언, 아무것도 적어주지 않으면 GET
def post():                                  #위 구문이 빠지면 client에서 form으로 정보를 보내도 서버쪽에서 받지 못함
    if request.method == 'POST':             #POST형식이면 if문을 실행
        value = request.form['test']         #post.html문서의 form태그의 정보를 변수에 저장
        return value                         #Get형식으로 /post에 접근하면 sorry출력
    else:
        return 'sorry'

if __name__ == '__main__':
    app.run()