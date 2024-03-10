from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def verify():
  pass

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/~')
def screen():
  return render_template('index.html')

app.run(debug=True)