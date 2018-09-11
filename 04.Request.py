# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login', methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['myName'] #form태그에서 Post로 받으면 실행
      return redirect(url_for('success', name = user))
   else:
      user = request.args.get('myName') #from태그에서 get으로 받으면 실행
      return redirect(url_for('success', name = user))

if __name__ == '__main__':
   app.run(debug = True)