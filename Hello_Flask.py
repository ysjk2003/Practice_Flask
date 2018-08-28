#-*- coding: utf-8 -*-
#utf-8로 인코딩
from flask import Flask

app = Flask(__name__)  #객체 생성

@app.route('/')  #root에 라우팅
def hello_flask():  #특정 URL을 호출했을 때 호출되는 함수 정의, 뷰 함수라고 함
    return 'Hello Flask!'

if __name__ == '__main__':  #실행되는 모듈이 파이썬 인터프리터에 의해 메인 모듈로 실행됐는지 임포트되어 사용됐는지 확인하여
    app.run()               #메인 모듈로 실행됐으면 테스토 용도로 사용되는 로컬 서버인 run()함수를 실행한다.