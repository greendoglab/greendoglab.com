#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import json
from flask import Flask, render_template, url_for, request
from flask_flatpages import FlatPages
from datetime import datetime
from flask_frozen import Freezer
import markdown
from urlparse import urljoin

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# config
DEBUG = False
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_MARKDOWN_EXTENSIONS = ['nl2br', 'tables', 'attr_list', 'extra']
FLATPAGES_AUTO_RELOAD = True
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POSTS_DIR = 'blog'
PAGES_DIR = 'page'
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
def mark(value):
    return markdown.markdown(value, FLATPAGES_MARKDOWN_EXTENSIONS)


def dateformat(value, format='%Y-%m-%d'):
    return value.strftime(format)


def timeformat(value, format='%H:%M'):
    return value.strftime(format)


app.jinja_env.filters['dateformat'] = dateformat
app.jinja_env.filters['timeformat'] = timeformat
app.jinja_env.filters['mark'] = mark


# functions
def get_json_data(josnfile):
    file_to_read = josnfile
    file_to_parse = os.path.join(os.path.dirname(__file__), "content", file_to_read)
    json_file = open(file_to_parse, "r")
    return json.load(json_file)


def sorted_posts(posts_list, sort_by):
    return sorted(posts_list, reverse=True, key=lambda p: p.meta[sort_by])


# get tags
def get_tags():
    z = (i.meta['tags'] for i in get_posts())
    f = []
    for i in z:
        for a in i:
            f.append(a)
    tags = sorted(set(f))
    return tags


# get tagged posts
def get_taget(posts_list, tag):
    tagged = [p for p in posts_list if tag in p.meta.get('tags', [])]
    tagged = sorted_posts(tagged)
    return tagged


# get posts
def get_posts(directory, sort_by):
    content = [p for p in pages if p.path.startswith(directory)]
    posts = sorted_posts(content, sort_by)
    return posts


def get_years(pages):
    years = list(set([page.meta.get('date').year for page in pages]))
    years.reverse()
    return years


@app.context_processor
def site_config():
    return {'site_config': get_json_data('config.json')}


# views
@app.route('/')
def index():
    page = pages.get('pages/index')
    return render_template('home.html', page=page)


# single page
# @app.route('/<path:path>/')
# def page(path):
#     work = pages.get_or_404(path)
#     template = 'work.html'
#     return render_template(template, work = work)


@app.route('/404.html')
def error404():
    return render_template('404.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# freezer
def make_external(url):
    return urljoin(request.url_root, url)


@freezer.register_generator
def pages_frozen():
    for page in pages:
        yield '/%s/' % page.path


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000, debug=True)
