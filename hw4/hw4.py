# Name: Alfredo Hernandez
# Class: CST 205
# Date: 4/11/2021
# Description: Used for displaying image info in templates. Uses flask.

from flask import (Flask,render_template)
from flask_bootstrap import Bootstrap
from image_info import image_info
from PIL import Image
import random

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def homepage():
    random.shuffle(image_info)
    
    return render_template('homepage.html', images = image_info[0:3])

@app.route('/picture/<id>')
def pic(id):
    for i in range(len(image_info)):
        if image_info[i]['id'] == id:
            author = image_info[i]['flickr_user']
            title = image_info[i]['title']
            tags = image_info[i]['tags']
    
    im = Image.open('static/images/' + id +'.jpg')
    image_mode = im.mode
    format = im.format
    width = im.width
    height = im.height

    return render_template('picture.html', id = id, author = author, tags = tags, title = title, image_mode = image_mode, format = format, width = width, height = height)