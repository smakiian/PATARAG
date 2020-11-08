from flask import Flask,request,render_template,jsonify
from app import app
import codecs
import json

@app.route('/')
@app.route('/index')
def index():
    with codecs.open(r"D:\Shagane\PATARAG\app\patarag-text\arm.txt", 'r', encoding="utf-8") as arm:
        armtext = arm.readlines()


    with open(r"D:\Shagane\PATARAG\app\patarag-text\rus.txt", 'r', encoding="utf-8") as rus:
        rustext = rus.readlines()

    with open(r"D:\Shagane\PATARAG\app\patarag-text\translit.txt", 'r', encoding="utf-8") as trl:
        trltext = trl.readlines()

    return render_template('index.html', title='Home', armtext=armtext, trltext=trltext, rustext=rustext)
