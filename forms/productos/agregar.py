from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField,TextAreaField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class Form(FlaskForm):
    pro_nombre = StringField('pro_nombre', validators=[DataRequired(message='Nombre requerido.')])
    pro_precio = DecimalField('pro_precio', validators=[DataRequired(message='Precio debe ser un numero decimal valido.')])
    pro_descripcion = TextAreaField('pro_descripcion', validators=[DataRequired(message='Descripcion requerida.')])
    pro_img         =  FileField('Upload Image', validators=[FileRequired(), FileAllowed(['jpg','jpeg','png','gif'],"Formato de imagen no soportado ")])