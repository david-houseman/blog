import git
from slugify import slugify
import datetime as dt
import pytz
import json
import datetime

from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

def git_version():
    commit = git.Repo().head.commit
    git_shorthash = commit.hexsha[:8]

    tz = pytz.timezone('Australia/Sydney')
    git_time = dt.datetime.fromtimestamp(commit.committed_date, tz).strftime('%Y-%m-%d %H:%M:%S %Z%z')
    git_author = commit.author.name
    return "{} [{}] by {}.".format(git_shorthash, git_time, git_author)

class Post:
    def __init__(self, header):
        self.title = header['title']
        self.author = header['author']
        self.date = header['date']
        self.slug = '{}-{}'.format(self.date.replace('-', ''), slugify(self.title))
        self.content = '/static/blog/{}/body.html'.format(self.slug)

with open('static/blog/contents.json', 'r') as f:
    posts = json.load(f)
    
posts = [Post(post) for post in posts]
posts.sort(key=lambda p: p.date, reverse=True)    

navigation_bar=[('index', 'Home'),
                ('blog', 'Blog')]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           navigation_bar=navigation_bar,
                           content='static/main/main.html',
                           git_version=git_version())


@app.route('/blog')
def blog():
    return render_template('blog.html',
                           navigation_bar=navigation_bar,
                           posts=posts,
                           git_version=git_version())


@app.route('/blog/<any({}):path>'.format(str([post.slug for post in posts])[1:-1]))
def render_post(path):
    post = next(post for post in posts if post.slug == path)    
    return render_template('post.html',
                           navigation_bar=navigation_bar,
                           post=post,
                           git_version=git_version())
