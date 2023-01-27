from flask import Flask,render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash


app = Flask(__name__)

app.config["SECRET_KEY"] = 'hardsecretkey'
app.config["SESSION_TYPE"] = 'filesystem'
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:''@localhost/python'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
app.app_context().push()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))


    def __init__(self, username, password):
        self.username = username
        self.password = self.__create_password(password)
    def __create_password(self,password):
        return generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_user, password)



@app.route("/")
def home():
    return render_template('index.html')


if(__name__ == '__main__'):
    #utils.crear_usuario()
    db.create_all()
    app.run(debug=True)