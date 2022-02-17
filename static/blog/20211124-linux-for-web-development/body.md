This simple website is powered by Debian Linux 11. It

- is written in `python`
- uses `git` version control
- uses the `flask` web framework
- uses `bootstrap` styling
- renders posts from markdown using `pandoc` and `mathjax`.

A preview web server for development purposes can be viewed using

    $ FLASK_APP=app
    $ FLASK_ENV=development
    $ flask run

and directing a web browser to `http://127.0.0.1:5000/`.

The source code for this website is viewable at
[github.com](https://github.com/david-houseman/blog).