import os
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

app = Flask('__main__')

@app.route('/')
def hello_world():
    request.args.get('name')
    return request.query_string

if app.name == '__main__':
    app.run()