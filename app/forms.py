from flask_wtf import FlaskForm #help us to create  the form Class
from wtforms import StringField,TextAreaField,SubmitField 
from wtforms.validators import Required #validator that preventthe users from submitting form without filling it.

class ReviewForm(FlaskForm):
    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')