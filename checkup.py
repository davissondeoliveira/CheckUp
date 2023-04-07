from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def checkup():
    return render_template('index.html', content='try me')

@app.route('/<name>')
def user(name):
    return f'Hello {name}!'

@app.route('/admin')
def admin():
	return redirect(url_for('checkup'))

@app.route('/about')
def about():
	return render_template('about.html')