from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Spiderman'}
    # return render_template('index.html',title = 'Home', templateuser = user)
    return render_template('index.html', templateuser = user)
