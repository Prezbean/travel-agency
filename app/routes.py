from flask import render_template, url_for
from app import app

@app.route('/home')
def home():
    return render_template('home.html', title = 'Home')

@app.route('/spring')
def spring():
    return render_template('season.html', season = 'spring')

@app.route('/summmer')
def summer():
    return render_template('season.html', season = 'summer')

@app.route('/autumn')
def autumn():
    return render_template('season.html', season = 'autumn')

@app.route('/winter')
def winter():
    return render_template('season.html', season = 'winter')