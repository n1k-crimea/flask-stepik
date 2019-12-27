# -*- coding: utf-8 -*-
from flask import Flask, render_template
from data import tours, title, subtitle, description, departures
from random import shuffle

app = Flask(__name__)

meta_data = {'title': title, 'subtitle': subtitle, 'description': description}


@app.route('/')
def index():
    tours_main_page = {}
    rn = list(range(1, len(tours) + 1))
    shuffle(rn)
    rn = rn[:6]
    for i in rn:
        tours_main_page[i] = tours[i]
    return render_template('index.html', meta_data=meta_data, departures=departures, tours=tours_main_page)


@app.route('/from/<direction>')
def direction(direction):
    tours_direction = {}
    departure_ru = ''
    for key, val in tours.items():
        if val['departure'] == direction:
            tours_direction[key] = val
    for key, val in departures.items():
        if key == direction:
            departure_ru = val
    price_list = [val['price'] for key, val in tours_direction.items()]
    nights_list = [val['nights'] for key, val in tours_direction.items()]
    meta_departure = {'departure': departure_ru, 'count_tours': len(tours_direction), 'min_price': min(price_list),
                      'max_price': max(price_list), 'min_nights': min(nights_list), 'max_nights': max(nights_list)}
    return render_template('direction.html', meta_data=meta_data, departures=departures,
                           tours_direction=tours_direction, meta_departure=meta_departure)


@app.route('/tour/<id>')
def tour(id):
    id = int(id)
    return render_template('tour.html', meta_data=meta_data, departures=departures, tour=tours[id])


if __name__ == '__main__':
    app.run()
