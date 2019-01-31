from flask import Flask
from sqlalchemy import BigInteger, Column, Float, Integer, Text
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request

app = Flask(__name__,
template_folder="../client/templates",
static_folder="../client/static"
)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///airports.sqlite'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=["POST"])
def register():
    user_name = request.form['user_name']
    user_email = request.form['user_email']
    user_city = request.form['user_city']
    return render_template('toy_upload.html')