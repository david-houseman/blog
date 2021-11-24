import os
import sys
import glob
import markdown as md
import datetime

from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



class Post:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.title = f.readline().lstrip('title:').strip()
            self.author = f.readline().lstrip('author:').strip()
            self.date = f.readline().lstrip('date:').strip()
            self.body = md.markdown(f.read())

            print(self.body)
            
@app.route('/blog')
def blog():
    posts = [Post(filename) for filename in glob.glob('blog/*md')]    
    return render_template('blog.html', posts=posts)
