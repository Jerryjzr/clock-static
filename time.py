#!/bin/python3
from flask import Flask,Response,redirect,request
import datetime
import time
from flask import Flask, render_template

app=Flask(__name__)

@app.get('/')
def gohome():

    return redirect('http://127.0.0.1:5000/static/index.html',code=301)
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
