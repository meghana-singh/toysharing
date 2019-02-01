from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

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

 
#db.create_all()
#db.session.commit()
