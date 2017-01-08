#!/usr/bin/env python

from flask import Flask
import os
import sys

app = Flask(__name__)

if not os.path.exists("config.cfg"):
    print("The config.cfg file does not exist.")
    sys.exit(1)
else:
    pipe_file = open("config.cfg").read()
    print("Writing to pipe '%s'." % pipe_file)

if not os.path.exists(pipe_file):
    print("The given pipe file does not exist.")
    sys.exit(1)
conduit = os.open(pipe_file, os.O_WRONLY)

@app.route("/")
def index():
    return "Hello, this is the index."

@app.route("/command/<command>")
def command(command):
    os.write(conduit, "%s\n" % command)
    return "Wrote '%s' to all clients." % command

if __name__ == '__main__':
    app.run()
