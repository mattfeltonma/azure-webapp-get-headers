import logging
import json
from flask import Flask, render_template, request, redirect

# Setup up a Flask instance
app = Flask(__name__)

# Render the template
@app.route("/")

def index():
    print(request.headers)
    print('---------------------------')
    return render_template('index.html', headers=request.headers)
