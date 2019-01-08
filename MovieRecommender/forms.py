from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired

GEN_CHOICES = ('action', 'adventure', 'animation', 'biography', 'comedy', 'crime', 'documentary', 'drama', 'family', 'fantasy', 'film noir', 'history', 'horror', 'music', 'musical', 'mystery', 'romance', 'sci-fi', 'short', 'sport', 'superhero', 'thriller', 'war', 'western')

class RecommendForm(FlaskForm):
  genre = SelectField(label='Choose Preferred Genre', choices = [(gen, gen) for gen in GEN_CHOICES], validators=[DataRequired()])
  ldur = IntegerField('Minimum Duration in mins', validators=[DataRequired()])
  udur = IntegerField('Maximum Duration in mins', validators=[DataRequired()])
  lyear = IntegerField('From Year', validators=[DataRequired()])
  uyear = IntegerField('To Year', validators=[DataRequired()])
  submit = SubmitField('Submit')