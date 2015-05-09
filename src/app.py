#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import json
from flask import Flask, render_template, url_for, request
from flask_flatpages import FlatPages
from datetime import date, datetime
from flask_frozen import Freezer
import markdown

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# config
DEBUG = False
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_MARKDOWN_EXTENSIONS = ['nl2br', 'tables', 'attr_list', 'extra']
FLATPAGES_AUTO_RELOAD = True
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

# templatetags
def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)

app.jinja_env.globals['url_for_other_page'] = url_for_other_page

def mark(value):
    return markdown.markdown(value, FLATPAGES_MARKDOWN_EXTENSIONS)

app.jinja_env.filters['mark'] = mark

# functions
def sorted_posts(posts_list, sort_by):
    return sorted(posts_list, reverse=True, key=lambda p: p.meta[sort_by])

# get posts
def get_posts(directory, sort_by):
    content = [p for p in pages if p.path.startswith(directory)]
    posts = sorted_posts(content, sort_by)
    return posts

def make_external(url):
    return urljoin(request.url_root, url)


# views
@app.route('/')
def index():
    json_file = open(os.path.join(os.path.dirname(__file__), "content", "works.json"), "r")
    works = json.load(json_file)
    works.reverse()
    page = pages.get('pages/index')
    return render_template(
            'home.html',
            page = page,
            works = works
    )

# single page
@app.route('/<path:path>/')
def page(path):
    work = pages.get_or_404(path)
    template = 'work.html'
    return render_template(template, work = work)


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
