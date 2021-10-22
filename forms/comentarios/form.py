from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField,TextAreaField
from wtforms.validators import DataRequired


class Form(FlaskForm):
    com_comentario = TextAreaField('com_comentario', validators=[DataRequired(message='Comentario requerido.')])

