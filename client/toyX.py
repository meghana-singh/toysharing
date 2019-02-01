from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
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

@app.route('/register')
def register():
   return render_template('register.html')
