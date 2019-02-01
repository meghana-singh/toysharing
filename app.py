from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy

from server import create_app
#from models import Parent, Toy, ToyParent

app = create_app()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///toy_share.sqlite'
db = SQLAlchemy(app)


class Parent(db.Model):
    __tablename__ = 'parent'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(255))
    city = db.Column(db.Text(255))
    mail = db.Column(db.Text(150))

class Toy(db.Model):
    __tablename__ = 'toy'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(255))
    age_cat = db.Column(db.Text(255))
    type_cat = db.Column(db.Text(255))
    picture = db.Column(db.Text(255))
    status = db.Column(db.Boolean)


class ToyParent(db.Model):
    __tablename__ = 'toy_parent'

    id = db.Column(db.Numeric, primary_key=True)
    id_toy = db.Column(db.Integer, nullable=False)
    id_parent = db.Column(db.Integer, nullable=False)

#db.create_all()

def update_user_table(user_name, user_email, user_city):
    db.session.add(Parent(name = user_name, city = user_city, mail = user_email))
    db.session.commit()

def update_toy_table(toyname, desc, agedropdown, catdropdown):
    print("called update_toy_table")
    db.session.add(Toy(name = toyname, desc = desc, age_cat = agedropdown, type_cat = catdropdown))
    db.session.commit()

def query_toy_table(agel, catl):
    toy = Toy.query.filter_by(age_cat=agel, type_cat=catl).all()
    return(toy)


@app.route("/")
def index():
    return render_template('main.html')

@app.route('/toy_upload')
def toyupload():
    print("printing from toyupload fn")
    return render_template('toy_upload.html')

@app.route('/toyupload_user', methods=['POST'])
def toyupload_user():
    print("printing from toyuploaduser fn")
    toyname = request.form['toyname']
    desc = request.form['desc']
    agedropdown = request.form['agedropdown']
    catdropdown = request.form['catdropdown']
    print("agedrop %s" % agedropdown)
    update_toy_table(toyname, desc, agedropdown, catdropdown)
    return render_template('/toyupload_user.html')

@app.route('/toy_query')
def toyquery():
    return render_template('toy_query.html')

@app.route('/query', methods=['POST'])
def query():
    print("in fn query")
    age = request.form['agel']
    cat = request.form['catl']
    print("agel %s" % age)
    toys = query_toy_table(age, cat)
    return render_template('toy_results.html', options=toys)
    

@app.route('/login')
def login():
    #check_user_table(user_email)
    return render_template('login.html')

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/register_user', methods=['POST'])
def register_user():
   user_name = request.form['user_name']
   user_email = request.form['user_email']
   user_city = request.form['user_city']
   update_user_table(user_name, user_email, user_city)
   return render_template('/toy_upload.html') 
