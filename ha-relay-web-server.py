#!/usr/bin/env python

from flask import Flask
import os
import sys

app = Flask(__name__)

if not os.path.exists(pipe):
    print("The given pipe file does not exist.")
    sys.exit(1)
conduit = os.open(pipe, os.O_WRONLY)

@app.route("/")
def index():
    return "Hello, this is the index."

@app.route("/command/<command>")
def command(command):
    os.write(conduit, "%s\n" % command)
    return "Wrote '%s' to all clients." % command

if __name__ == '__main__':
    app.run()
