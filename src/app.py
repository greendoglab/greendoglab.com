#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# config
DEBUG = False
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_MARKDOWN_EXTENSIONS = ['nl2br', 'tables', 'attr_list', 'extra']
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
WORKS_DIR = 'works'
PROJECTS_DIR = 'projects'
PAGES_DIR = 'pages'
ESTI_DIR = 'testimonials'
PER_PAGE = 5
FEED_MAX_LINKS = 5

FREEZER_DESTINATION = '../production'
FREEZER_RELATIVE_URLS = False

# app
app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)


@app.context_processor
def let_work_data():
    lets_work = pages.get('home/lets-work')
    return dict(lets_work=lets_work)


# views
@app.route('/')
def index():
    ui = pages.get('home/ui')
    front = pages.get('home/front')
    back = pages.get('home/back')
    why = pages.get('home/why')
    about = pages.get('home/about')
    return render_template(
        'home.html',
        ui=ui,
        front=front,
        back=back,
        why=why,
        about=about
    )


# single page
@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    template = 'page.html'
    return render_template(template, page=page)


@app.route('/404.html')
def error404():
    return render_template('404.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# freezer
@freezer.register_generator
def pages_frozen():
    for page in pages:
        yield '/%s/' % page.path


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000, debug=True)
