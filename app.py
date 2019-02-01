from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy

from server import create_app
#from models import Parent, Toy, ToyParent

app = create_app()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///toy_share.sqlite'
db = SQLAlchemy(app)


class Parent(db.Model):
    __tablename__ = 'parent'

    id = db.Column(db.Numeric, primary_key=True)
    name = db.Column(db.Text(255))
    city = db.Column(db.Text(255))
    mail = db.Column(db.Text(150))

class Toy(db.Model):
    __tablename__ = 'toy'

    id = db.Column(db.Numeric, primary_key=True)
    name = db.Column(db.Text(255))
    age_cat = db.Column(db.Text(255))
    type_cat = db.Column(db.Text(255))
    picture = db.Column(db.Text(255))


class ToyParent(db.Model):
    __tablename__ = 'toy_parent'

    id = db.Column(db.Numeric, primary_key=True)
    id_toy = db.Column(db.Integer, nullable=False)
    id_parent = db.Column(db.Integer, nullable=False)

db.create_all()


@app.route("/")
def index():
    return render_template('main.html')

@app.route('/toy_upload')
def toyupload():
   return render_template('toy_upload.html')

@app.route('/toy_query')
def toyquery():
   return render_template('toy_query.html')

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
   user_name = request.form['user_name']
   user_email = request.form['user_email']
   user_city = request.form['user_city']
   update_user_table(user_name, user_email, user_city)
   return render_template('register.html')