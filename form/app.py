import os
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

app = Flask('__main__')

@app.route('/')
def hello_world():
    return request.data

if app.name == '__main__':
    app.run()