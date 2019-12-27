# -*- coding: utf-8 -*-
from flask import Flask, render_template
from data import tours, title, subtitle, description, departures
from random import shuffle

app = Flask(__name__)

meta_data = {'title': title, 'subtitle': subtitle, 'description': description}

def find_end(n:int, val:str):
    if val == 'tours':
        if n in [11, 12, 13, 14]:
            return 'туров'
        else:
            if str(n)[-1] in ['1']:
                return 'тур'
            elif str(n)[-1] in ['2', '3', '4']:
                return 'тура'
            else:
                return 'туров'
    elif val == 'nights':
        if n in [11, 12, 13, 14]:
            return 'ночей'
        else:
            if str(n)[-1] in ['1']:
                return 'ночь'
            elif str(n)[-1] in ['2', '3', '4']:
                return 'ночи'
            else:
                return 'ночей'


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
    count_tours = len(tours_direction)
    '''if count_tours in [11, 12, 13, 14]:
        ending = 'туров'
    else:
        if str(count_tours)[-1] in ['1']:
            ending = 'тур'
        elif str(count_tours)[-1] in ['2', '3', '4']:
            ending = 'тура'
        else:
            ending = 'туров'''
    price_list = [val['price'] for key, val in tours_direction.items()]
    nights_list = [val['nights'] for key, val in tours_direction.items()]

    meta_departure = {'departure': departure_ru, 'count_tours': count_tours, 'ending': find_end(count_tours, 'tour'),
                      'min_price': min(price_list),
                      'max_price': max(price_list), 'min_nights': {'count': min(nights_list), 'ending': find_end(min(nights_list), 'nights')}, 'max_nights': {'count': max(nights_list), 'ending': find_end(max(nights_list), 'nights')}}
    return render_template('direction.html', meta_data=meta_data, departures=departures,
                           tours_direction=tours_direction, meta_departure=meta_departure)


@app.route('/tour/<id>')
def tour(id):
    id = int(id)
    return render_template('tour.html', meta_data=meta_data, departures=departures, tour=tours[id])


if __name__ == '__main__':
    app.run()
