from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///toy_share.db'
db = SQLAlchemy(app)


class Forbes(db.Model):

    __tablename__ = 'forbes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    country = db.Column(db.String)
    sales = db.Column(db.Float)
    profits = db.Column(db.Float)
    assets = db.Column(db.Float)
    marketvalue = db.Column(db.Float)

    def __repr__(self):
        return (f"<Forbes(name='{self.name}',"
                f" country={self.country}, profits=={self.profits}>")

#db.create_all()



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

 

db.session.add(new_bean)
db.session.commit()

#C