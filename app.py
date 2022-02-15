import os
import sys
import glob
import json
import datetime

from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

def git_version():
    git_shorthash = "Unknown"
    git_time = "00:00"
    git_author = "Unknown"

    git_output = (
        os.popen("git show --format='%h%n%ai%n%an'").read().splitlines()
    )

    if len(git_output) >= 3:
        git_shorthash = git_output[0]
        git_time = git_output[1]
        git_author = git_output[2]

    return "{} [{}] by {}.".format(git_shorthash, git_time, git_author)

navigation_bar=[('index', 'Home'),
                ('blog', 'Blog')]

@app.route('/')
@app.route('/index')
def index():
    with open('main.html', 'r') as f:
        main = f.read()
        
    return render_template('index.html',
                           navigation_bar=navigation_bar,
                           main=main,
                           git_version=git_version())


class Post:
    def __init__(self, dirname):
        with open(os.path.join(dirname, 'head.json'), 'r') as f:
            header = json.load(f)
            self.title = header['title']
            self.author = header['author']
            self.date = header['date']

        with open(os.path.join(dirname, 'body.html'), 'r') as f:
            self.body = f.read()

            
@app.route('/blog')
def blog():
    posts = [Post(dirname) for dirname in glob.glob('static/blog/202*')]
    posts.sort(key=lambda p: p.date, reverse=True)
    
    return render_template('blog.html',
                           navigation_bar=navigation_bar,
                           posts=posts,
                           git_version=git_version())
