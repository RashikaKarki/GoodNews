import os
from flask import Flask,jsonify, request
from Script.scrape import get_data
import json

app = Flask(__name__)

@app.route('/get_data', methods=['GET','POST'])
def get_d():
    if request.method == 'GET':
        data = get_data()
        with open('Data/data.json', 'w') as fp:
            json.dump(data, fp)
        return jsonify(data)