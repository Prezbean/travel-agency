from flask import render_template, url_for
from app import app

@app.route('/home')
def home():
    return render_template('home.html', title = 'Home')

@app.route('/spring')
def spring():
    return render_template('season.html', title = 'Spring')

@app.route('/summmer')
def summer():
    return render_template('season.html', title = 'Summer')

@app.route('/autumn')
def autumn():
    return render_template('season.html', title = 'Autumn')

@app.route('/winter')
def winter():
    return render_template('season.html', title = 'Winter')