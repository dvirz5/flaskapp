from flaskext.mysql import MySQL
from flask import Flask,request
from flask import json
import sys
from flask import Flask, render_template, json, request

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')
if __name__ == "__main__":
    app.run()
