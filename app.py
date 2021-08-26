from flask import Flask, render_template
from random import choice, sample, randint

from flask_debugtoolbar import DebugToolbarExtension


COMPLIMENTS = ["cool", "clever", "tenacious", "awesome", "Pythonic"]

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)


@app.route('/')
def index():
    """Return homepage."""

    return render_template("home.html")