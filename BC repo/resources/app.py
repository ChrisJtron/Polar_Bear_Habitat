from flask import Flask, jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS (app)

@app.route('/')
def home():
    return 'Polar Bear Tracker 1986-2016'

@app.route('/data')
def fetch():
    results=[]
    return jsonify(results)

if __name__ == '__main__':
    app.debug = True
    app.run()