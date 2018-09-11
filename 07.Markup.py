# -*- coding: utf-8 -*-

from flask import Flask, Markup, render_template

app = Flask(__name__)

@app.route('/')
def index():
    markup1 = Markup(u'<strong>Hello %s!</strong>') % '<blink>hacker</blink>' #여기에선 strong태그는 적용되지만 blink태그는 적용되지 않고 그대로 출력된다
    markup2 = Markup.escape('<blink>hacker</blink>')   #blink까지 그대로 출력
    markup3 = Markup('<em>Marked up</em> &raquo; HTML').striptags() #태그제거 &raquo는 hex값으로 바뀐다.
    render_template('markup.html', markup1=markup1, markup2=markup2, markup3=markup3)
    return render_template('markup.html', markup1=markup1, markup2=markup2, markup3=markup3)
    #Markup클래스는 특수문자들을 HTML로 적용되지 못하게 막아준다

if __name__ == '__main__':
    app.run()