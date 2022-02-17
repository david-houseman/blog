import os
import git
import slugify
import time
import json
import datetime

from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

def git_version():
    commit = git.Repo().head.commit
    git_shorthash = commit.hexsha[:8]
    git_time = time.asctime(time.gmtime(commit.committed_date))
    git_author = commit.author.name
    return "{} [{} UTC] by {}.".format(git_shorthash, git_time, git_author)


navigation_bar=[('index', 'Home'),
                ('blog', 'Blog')]

@app.route('/')
@app.route('/index')
def index():
    with open('static/main/main.html', 'r', encoding='utf-8') as f:
        main = f.read()
        
    return render_template('index.html',
                           navigation_bar=navigation_bar,
                           main=main,
                           git_version=git_version())


class Post:
    def __init__(self, header):

        self.title = header['title']
        self.author = header['author']
        self.date = header['date']
        self.dirname = '{}-{}'.format(self.date.replace('-', ''), slugify(self.title))
        
        with open(os.path.join(self.dirname, 'body.html'), 'r', encoding='utf-8') as f:
            self.body = f.read()

            
@app.route('/blog')
def blog():
    with open('static/blog/contents.json', 'r') as f:
        posts = json.load(f)
    
    posts = [Post(post) for post in posts]
    posts.sort(key=lambda p: p.date, reverse=True)
    
    return render_template('blog.html',
                           navigation_bar=navigation_bar,
                           posts=posts,
                           git_version=git_version())
