from flask import Flask, render_template, abort, make_response

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('page_not_found.html'), 404)
    #response에 reder_template()을 넣고 status에 404를 넣음
    resp.headers['X-Something'] = 'A value'
    #header 추가 dictionary형태이 아마도?
    return resp

@app.route('/')
def index():
    abort(404)

if __name__ == '__main__':
    app.run()

#(Response, status, headers)