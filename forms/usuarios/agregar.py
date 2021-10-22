from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length


def validar_rol(form, field):
    if field.data not in ['superadministrador', 'administrador', 'usuariofinal']:
        raise ValidationError('Rol no valido.')


class Form(FlaskForm):
    usu_usuario = StringField('usu_usuario', validators=[DataRequired()])
    usu_email = EmailField('usu_email', validators=[DataRequired(), Email()])
    usu_password = PasswordField('usu_password', validators=[
        DataRequired(message="Contraseña requerida"),
        EqualTo('usu_password2', message='Las contraseñas deben ser iguales'),
        Length(min=6, message='La contraseña debe tener al menos 6 caracteres')
    ])
    usu_password2 = PasswordField('usu_password', validators=[DataRequired()])
    usu_nombres = StringField('usu_nombres', validators=[DataRequired()])
    usu_apellidos = StringField('usu_apellidos', validators=[DataRequired()])
    usu_rol = SelectField(
        u'Rol',
        choices=[
            ('', 'Seleccionar...'),
            ('superadministrador', 'Super Administrador'),
            ('administrador', 'Administrador'),
            ('usuariofinal', 'Usuario Final')
        ],
        validators=[DataRequired(), validar_rol])
