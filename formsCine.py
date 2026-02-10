from wtforms import (EmailField, Form, IntegerField, PasswordField, RadioField,
                     StringField, validators)


class cineForm(Form):
    nombre=StringField('Nombre', [validators.DataRequired(message='El nombre es requerido')])
    cCompradores=IntegerField('Cantidad Compradores',[validators.DataRequired(message='El numero de compradores es requerido'), validators.NumberRange(min=1, max=7, message='Máximo 7 compradores')])
    cBoletas=IntegerField('Cantidad Boletas',[validators.DataRequired(message='El campo es requerido'), validators.NumberRange(min=1, max=7, message='Máximo 7 boletas')])
    tarjeta = RadioField("Tarjeta cineco",choices=[("si", "SI"), ("no", "NO")], validators=[validators.DataRequired(message='Debe seleccionar una opcion')],default="no")