import os
from flask import Flask,jsonify, request
from Script.scrape import get_data
import json

app = Flask(__name__)

@app.route('/get_data', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        data = get_data()
        with open('Data/data.json', 'w') as fp:
            json.dump(data, fp)
        return jsonify(data)

@app.route('/view_data', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        with open('Data/data.json', 'r') as fp:
            data = fp
        return jsonify(data)