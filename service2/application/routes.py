from flask import render_template, redirect, url_for, Response, request
from application import app
import requests 
import random

@app.route('/')
@app.route('/name', methods=['GET'])
def getname():
	animals = [
		'Dog',
		'Cat',
		'Tiger',
		'Cow',
		'Owl'
		]
	animal = animals[random.randrange(5)]
	return Response(animal,mimetype='text/plain')

@app.route('/noise', methods=['GET','POST'])
def animalnoise():
	noises={
		"Dog": "Woof",
		"Cat" : "Meow",
		"Tiger" : "Roar",
		"Cow" : "Moo",
		"Owl" : "Hoot! Hoot!"
	}

	data_sent = request.data.decode('utf-8')
	noise = noises[data_sent]
	return Response(noise, mimetype='text/plain') 