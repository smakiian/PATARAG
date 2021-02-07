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

    return render_template('liturgy_three_lang.html', title='Liturgy', armtext=text_dict['a'], trltext=text_dict['t'], rustext=text_dict['r'])

@app.route('/liturgy-arm')
def liturgia_arm():
    text = []
    path = os.path.normpath(os.getcwd() + f"/app/patarag-text/a")
    for i in sorted(os.listdir(path)):
        with codecs.open(os.path.join(path, i), "r", encoding="utf-8") as f:
            text.append(f.readlines())

    return render_template('liturgy_single_lang.html', title='Liturgy-arm', text=text)

@app.route('/liturgy-trl')
def liturgia_trl():
    text = []
    path = os.path.normpath(os.getcwd() + f"/app/patarag-text/t")
    for i in sorted(os.listdir(path)):
        with codecs.open(os.path.join(path, i), "r", encoding="utf-8") as f:
            text.append(f.readlines())

    return render_template('liturgy_single_lang.html', title='Liturgy-trl', text=text)

@app.route('/liturgy-rus')
def liturgia_rus():
    text = []
    path = os.path.normpath(os.getcwd() + f"/app/patarag-text/r")
    for i in sorted(os.listdir(path)):
        with codecs.open(os.path.join(path, i), "r", encoding="utf-8") as f:
            text.append(f.readlines())

    return render_template('liturgy_single_lang.html', title='Liturgy-rus', text=text)