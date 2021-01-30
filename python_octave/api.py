import os
from flask import Flask, jsonify
from runScripts import processFactorial, processFibonacci

app = Flask(__name__)

@app.route('/')
def welcome():
    return jsonify({'status': 'Api working!'})

@app.route('/factorial/<number>')
def factorial(number):
    result = processFactorial(int(number))
    return jsonify(result)

@app.route('/fibonacci/<number>')
def fibonacci(number):
    result = processFibonacci(int(number))
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')