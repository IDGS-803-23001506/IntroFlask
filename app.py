from flask import Flask, flash, render_template, request
from flask_wtf.csrf import CSRFProtect

import forms
import formsCine

app = Flask(__name__)

app.secret_key='clave secreta'
csrf=CSRFProtect()

@app.route('/index')
def index():
    titulo="IDGS803-Flask"
    lista=["pedro","mario","juan"]
    return render_template("index.html",titulo=titulo, lista=lista)

@app.route("/alumnos")
def alumnos():
    return render_template('alumnos.html')

@app.route("/usuario", methods=['GET', 'POST'])
def usuario():
    mat=0
    nom=''
    apa=''
    ama=''
    correo=''
    usuario_class=forms.userForm(request.form)
    if request.method=='POST' and usuario_class.validate():
        mat=usuario_class.matricula.data
        nom=usuario_class.nombre.data
        apa=usuario_class.apaterno.data
        ama=usuario_class.amaterno.data
        correo=usuario_class.email.data
        
    return render_template('usuario.html',form=usuario_class,mat=mat,nom=nom,apa=apa, ama=ama, correo=correo)

@app.route('/hola')
def hola():
    return "Hola, hello"

@app.route('/user/<string:user>')
def user(user):
    return f"Hello, {user}"

@app.route('/numero/<int:n>')
def numero(n):
    return f"Hello, {n}"

@app.route('/user/<int:id>/<string:name>')
def username(id,name):
    return f"<h1>!Hola, {name}! Tu ID es: {id}</h1>"

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1,n2):
    return f"<h1>La suma es: {n1 + n2}</h1>"

@app.route("/default/")
@app.route("/default/<string:param>")
def func(param="juan"):
    return f"<h1>Hola, {param}</h1>"


@app.route("/operas")
def operas():
    return '''
<form>
<label for="name">Name:</label>
<input type="text" id="name" name="name" required>

<label for="name">A paterno:</label>
<input type="text" id="name" name="name" required>

'''

@app.route("/operasBas",methods=['GET', 'POST'])
def operas1():
    res=0
    if request.method == 'POST':
        n1=request.form.get('n1')
        n2=request.form.get('n2')
        if request.form.get('operacion') =='sumar':
            res=float(n1)+float(n2)
        elif request.form.get('operacion') =='resta':
            res=float(n1)-float(n2)
        elif request.form.get('operacion') =='multiplicar':
            res=float(n1)*float(n2)
        elif request.form.get('operacion') =='division':
            res=float(n1)/float(n2)

    return render_template('operasBas.html', resultado= res)


@app.route("/resultado",methods=['GET', 'POST'])
def resultado():
    resultado = 0
    n1=request.form.get('n1')
    n2=request.form.get('n2')
    if request.form.get('operacion') =='sumar':
        resultado=float(n1)+float(n2)
    elif request.form.get('operacion') =='resta':
        resultado=float(n1)-float(n2)
    elif request.form.get('operacion') =='multiplicar':
        resultado=float(n1)*float(n2)
    elif request.form.get('operacion') =='division':
        resultado=float(n1)/float(n2)
    return f"<h1>El resultado es {resultado}</h1>"


@app.route ('/cinepolis', methods=['GET', 'POST'])
def cinepolis():
    nom=''
    com=0
    tar=''
    bol=0
    val=0
    total=0
    cinepolis_class=formsCine.cineForm(request.form)
    if request.method=='POST' and cinepolis_class.validate():
        nom=cinepolis_class.nombre.data
        com=cinepolis_class.cCompradores.data
        tar=cinepolis_class.tarjeta.data
        bol=cinepolis_class.cBoletas.data
    val = bol * 12
    if bol < 5:
        total = val * 0.85
    if bol == 3 or bol== 4 or bol == 5:
        total = val * 0.90
    if tar == 'si':
        total = total * .90
    return render_template('cinepolis.html', form=cinepolis_class,
                           nom=nom,com=com,tar=tar,bol=bol,total=total)


if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)
