import os
import sys
import glob
import markdown as md
import datetime

from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)


def git_version():
    git_shorthash = "Unknown"
    git_time = "00:00"
    git_author = "Unknown"

    git_output = (
        os.popen("git show --no-patch --format='%h%n%ai%n%an'").read().splitlines()
    )

    if len(git_output) == 3:
        git_shorthash = git_output[0]
        git_time = git_output[1]
        git_author = git_output[2]

    return "{} [{}] by {}.".format(git_shorthash, git_time, git_author)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           git_version=git_version())


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
    return render_template('blog.html',
                           posts=posts,
                           git_version=git_version())
