# -*- coding: utf-8 -*-
from flask import Flask, render_template
from data import tours, title, subtitle, description, departures
from random import shuffle

app = Flask(__name__)


@app.route('/')
def index():
    '''tours_main_page = {}
    rn = list(range(1,13))
    shuffle(rn)'''

    return render_template('index.html', site_title=title, site_subtitle=subtitle, site_desc=description)


@app.route('/from/<direction>')
def direction(direction):
    return render_template('direction.html')


@app.route('/tour/<id>')
def tour(id):
    id = int(id)
    return render_template('tour.html', tour=tours[id])


if __name__ == '__main__':
    app.run()
