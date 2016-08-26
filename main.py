#from flask import Flask, request, jsonify
from flask import Flask, render_template, request, jsonify
from db import *
import jsonpickle

app = Flask(__name__)

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
    user.username += "Q"
    #return render_template('login.html', model=user)
    #return json.dumps({par1:'OK','user':user,'pass':password});
    return jsonpickle.encode(user)

if __name__ == '__main__':
  app.run()

class User:
    username="daniel"

    password=""
