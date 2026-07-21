# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/aa')
def hello_world():
    return 'Hello, World from Flask!'

@app.route('/teste')
def teste():
    return 'teste aaaaaaa'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
