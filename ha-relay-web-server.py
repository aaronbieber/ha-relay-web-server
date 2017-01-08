#!/usr/bin/env python

from flask import Flask
import os

app = Flask(__name__)
conduit = os.open("/Users/airborne/Projects/conduit", os.O_WRONLY)

@app.route("/")
def index():
    return "Hello, this is the index."

@app.route("/command/<command>")
def command(command):
    os.write(conduit, "%s\n" % command)
    return "Wrote '%s' to all clients." % command

if __name__ == '__main__':
    app.run()
