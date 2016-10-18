from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Wordcount service is online'

@app.route('/count', methods=['GET'])
def names():
    result = {"words" : long(request.args.get('number'))}
    return jsonify(result)
