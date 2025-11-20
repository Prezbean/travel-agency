from flask import render_template, url_for
from app import app

@app.route('/') # Decorator to get to home page
def home():
    return render_template('home.html', title = 'Home')

@app.route('/spring') # Decorator to get to spring page of season html file
def spring():
    return render_template('season.html', season = 'spring')

@app.route('/summer') # Decorator to get to summer page of season html file
def summer():
    return render_template('season.html', season = 'summer')

@app.route('/autumn') # Decorator to get to autumn page of season html file
def autumn():
    return render_template('season.html', season = 'autumn')

@app.route('/winter') # Decorator to get to winter page of season html file
def winter():
    return render_template('season.html', season = 'winter')