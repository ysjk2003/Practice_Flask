from flask import Flask, abort, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))  #리디렉션 함수

@app.errorhandler(404)          #사용자 정의 오류
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/login')
def login():
    abort(404)      #404 에러를 띄움
    this_is_never_executed()

if __name__ == '__main__':
    app.run()