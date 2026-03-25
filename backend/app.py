from flask import Flask,render_template,jsonify
from connections import coll
import os

env = os.environ
PORT = os.environ.get('PORT', 8000)

app = Flask(__name__)

@app.route('/')
def index():

    return jsonify({"message": "Backend is working!"}) 

@app.route('/api/get')
def api():

    names = coll.find()

    results = []
    for name in names:
        results.append(name['value'])

    results = {"data": results}


    return jsonify(results)

@app.route('/api/add/<name>') 
def add_name(name):
    coll.insert_one({'value': name})
    return jsonify({"message": "Name added successfully!"})

if __name__ == '__main__':
    app.run(debug=True, port=PORT, host='0.0.0.0')