from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Wordcount service is online'

@app.route('/count', methods=['GET'])
def count_words():
    count = long(request.args.get('number', ''))
    result = "Number of words in text: " + str(count)
    return result
