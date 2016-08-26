# -*- coding: utf-8 -*-

#from flask import Flask, request, jsonify
from flask import Flask, render_template, request, jsonify, flash
from db import *
import jsonpickle
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def login():
    #return jsonify(query_all_users())
    user = User()
    return render_template('login.html', model=user)

@app.route('/processLogin', methods=['POST'])
def processLogin():
    user = User()
    user.username = request.form['username']
    user.password = request.form['password']
    flash("Usuario y contraseña correctos (" + user.username + ")." )
    return render_template('login.html', model=user)
    #return json.dumps({par1:'OK','user':user,'pass':password});
    #return jsonpickle.encode(user)

if __name__ == '__main__':
  app.run()

class User:
    username="daniel"

    password=""
