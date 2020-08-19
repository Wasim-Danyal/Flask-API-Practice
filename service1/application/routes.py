from flask import render_template, redirect, url_for, request
from application import app
import requests

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')

@app.route('/generate', methods=['GET','POST'])
def generate():
	animal = requests.get('http://34.105.137.219:5001/name')
	rs = requests.get('http://34.105.137.219:5001/noise', data=animal.text)
	return render_template('generate.html', animalname = animal.text, animalsound = rs.text)
