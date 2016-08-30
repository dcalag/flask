# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify, flash
from db import *
from person import Person
#import jsonpickle
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def index():
    #return jsonify(query_all_users())
    person = Person()
    return render_template('personIndex.html', model=person)

@app.route('/processPerson', methods=['POST'])
def processPerson():
    # simul. delay:
    # sleep(1)
    person = Person()
    person.name = request.form['name']
    person.age = request.form['age']
    flash("Usuario: " + person.name + ", edad: " + person.age)
    return render_template('person.html', model=person)
    #return json.dumps({par1:'OK','user':user,'pass':password});
    #return jsonpickle.encode(user)

if __name__ == '__main__':
  app.run()
