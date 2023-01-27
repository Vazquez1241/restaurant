import time

from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import utils
import models
from flask.globals import session




app = Flask(__name__)

app.config["SECRET_KEY"] = 'hardsecretkey'
app.config["SESSION_TYPE"] = 'filesystem'


@app.route("/")
def home():
    session['usuario'] = 'invitado'
    session["en-linea"] = True
    return render_template('index.html', rango=session["usuario"], status=session['en-linea'])

@app.route('/logeo', methods=["POST","GET"])
def logeo():
    if(request.method == "POST"):
        user = request.form["username"]
        contrasenia = request.form["password"]

        return 'hola'

#
if(__name__ == '__main__'):
    #utils.crear_usuario()

    app.run(debug=True)