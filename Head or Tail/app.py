import random
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")

def index():
    num=random.randint(0,1)
    return render_template("index.html", number=num)
