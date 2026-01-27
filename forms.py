from wtforms import (EmailField, Form, IntegerField, PasswordField,
                     StringField, validators)


class userForm(Form):
    matricula=IntegerField('Matricula', [validators.DataRequired(message='El campo es requerido'),
                                         validators.NumberRange(min=2, max=100, message='ingresa un nombre valido')])
    nombre=StringField('Nombre',[validators.DataRequired(message='El campo es requerido'),validators.length(min=4,max=10,message='Ingrese nombre valido')])
    apaterno=StringField('Apaterno',[validators.DataRequired(message='El campo es requerido')])
    amaterno=StringField('Amaterno',[validators.DataRequired(message='El campo es requerido')])
    email=EmailField('Correo',[validators.Email(message='Inbgresa un correo valido')])