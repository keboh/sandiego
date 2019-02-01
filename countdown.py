from flask import Flask, render_template
import datetime
import time
import os


TIME_EPOCH = int(os.getenv("TIME"))
MESSAGE = os.getenv("MESSAGE")

app = Flask(__name__)


@app.route("/")
def index():
    date = TIME_EPOCH - int(time.time())
    return render_template("index.html", date=date, message=MESSAGE)
