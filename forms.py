from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """Add pets with this form."""
    name = StringField("Pet Name", validators=[InputRequired(message="Name cannot be blank")])
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Photo URL",[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=25)])
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)])

class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField("Photo URL",[Optional(), URL()])
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)])
    available = BooleanField("Available?") 
