from flask import Flask, render_template, redirect
from flask.globals import request
from flask_debugtoolbar import DebugToolbarExtension

from Stories import Story, story
from MadLibsForm import MadLibForm

COMPLIMENTS = ["cool", "clever", "tenacious", "awesome", "Pythonic"]

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)


@app.route('/')
def home():
    """Return homepage."""
    ex_story = story
    
    form = MadLibForm()
    
    msg = ""
    
    if form.validate_on_submit():
        place = form.place.data
        noun = form.noun.data
        verb = form.verb.data
        adjective = form.adjective.data
        plural_noun = form.plural_noun.data
        
        return redirect('/story')
    else: 
        msg = "Error"
    
    return render_template("home.html", form = form, story = ex_story, msg = msg)





@app.route('/story', methods=['POST'])
def post_story():
    """Return madlib story from form submit."""

    text = story.generate(request.form)
   
    return render_template("story.html", text=text)

# Refactored code to integrate with Stories class more efficiently
# but still want to keep this code!
    # place = request.form["place"]
    # noun = request.form["noun"]
    # verb = request.form["verb"]
    # adjective = request.form["adjective"]
    # plural_noun = request.form["plural_noun"]
 
    # madlib = Story(
    #     [place,
    #      noun, 
    #      verb, 
    #      adjective, 
    #      plural_noun
    #     ],
    #     """Once upon a time in a long-ago {place}, there lived a
    #     large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    # )

    # text = madlib.generate(request.form)
    
    # return render_template("story.html", text=text)
