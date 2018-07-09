## OU SECS Summer Camp
## Programming Gadgets
## Summer 2018
## Erik Fredericks
## hello-web.py

## Hello world of Flask
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello world!"
