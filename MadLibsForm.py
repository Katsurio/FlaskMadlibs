from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MadLibForm(FlaskForm):
    place = StringField('Place:', validators=[DataRequired()])
    noun = StringField('Noun:', validators=[DataRequired()])
    verb = StringField('Verb:', validators=[DataRequired()])
    adjective = StringField('Adjective:', validators=[DataRequired()])
    plural_noun = StringField('Plural Noun:', validators=[DataRequired()])
    submit = SubmitField('Submit')