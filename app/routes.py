from flask import Flask,request,render_template,jsonify
from app import app
import codecs
import json
import os

@app.route('/')
@app.route('/index')
def index():
    armtext = []
    a_path = os.path.curdir + r'\app\patarag-text\a'
    for i in sorted(os.listdir(a_path)):
        with codecs.open(os.path.join(a_path, i), 'r', encoding="utf-8") as arm:
            armtext.append(arm.readlines())

    trltext = []
    t_path = os.path.curdir + r'\app\patarag-text\t'
    for i in sorted(os.listdir(t_path)):
        with codecs.open(os.path.join(t_path, i), 'r', encoding="utf-8") as trl:
            trltext.append(trl.readlines())

    rustext = []
    r_path = os.path.curdir + r'\app\patarag-text\r'
    for i in sorted(os.listdir(r_path)):
        with codecs.open(os.path.join(r_path, i), 'r', encoding="utf-8") as rus:
            rustext.append(rus.readlines())

    return render_template('index.html', title='Home', armtext=armtext, trltext=trltext, rustext=rustext)
