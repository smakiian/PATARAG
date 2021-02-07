from flask import Flask,request,render_template,jsonify
from app import app
import codecs
import json
import os

@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', title='Home')

@app.route('/liturgy')
def liturgia():
    text_dict = {'a': [], 't': [], 'r': []}
    # "a" for armenian text
    # "t" for translitaration of armenian
    # "r" for russian text

    for j in text_dict:
        path = os.path.normpath(os.getcwd() + f"/app/patarag-text/{j}")
        for i in sorted(os.listdir(path)):
            with codecs.open(os.path.join(path, i), "r", encoding="utf-8") as f:
                text_dict[j].append(f.readlines())

    return render_template('liturgy.html', title='Liturgy', armtext=text_dict['a'], trltext=text_dict['t'], rustext=text_dict['r'])