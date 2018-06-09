#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 termninja <nmicovic@outlook.com>
#
# Distributed under terms of the MIT license.

from app import app
from flask import render_template
from flask import request
# from network.predict import predict
from network.generate import GenerativeNetwork

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='AI Gusle')

@app.route('/sepRandom', methods=['GET'])
def handle_sepRandom():
    generated_song = get_generated_song('')
    return render_template('show_generated_sep.html', title='SEP generator', song_title='SEP Generated song', song=generated_song)

model = GenerativeNetwork('./epic_songs.txt', 'app/static/model.yaml', 'app/static/weights.hdf5')

import tensorflow as tf

def predict(seed=''):
    seed = seed.encode('utf8')
    seed = model.make_seed(seed)
    generated = model.generate(seed)
    print('generated {}'.format(generated))
    generated = unicode(generated, 'utf-8', errors='ignore')
    return generated

def get_generated_song(seed=''):
    print(u'seed is "{}"'.format(seed))
    generated_song = predict(seed)
    generated_song = generated_song.split('\n')
    generated_song = map(lambda x: x.strip(), generated_song)
    generated_song = filter(lambda x: not(x == "" or x == "\n"), generated_song)
    generated_song = list(generated_song)
    return generated_song


@app.route('/sep', methods=['GET', 'POST'])
def handle_sep():
    if request.method == 'GET':
        return render_template('sep.html', title='SEP generator')
    elif request.method == 'POST':
        sep_seed = request.form['sep_seed']
        generated_song = get_generated_song(sep_seed)
        # generated_song = list(map(lambda x: x.encode('utf-8'), generated_song))
        # generated_song = ['Тестиранје', 'Unicoce ššćč']
        return render_template('show_generated_sep.html', title='SEP generator', song_title='SEP Generated song', song=generated_song)
    else:
        return 'Bad request'

@app.route('/deepdream', methods=['GET', 'POST'])
def handle_deepdream():
    if request.method == 'GET':
        return render_template('deepdream.html', title='DeepDream generator')
    elif request.method == 'POST':
        return 'TODO'
    else:
        return 'Bad request'


@app.route('/about', methods=['GET'])
def handle_about():
    if request.method == 'GET':
        return render_template('about.html', title='About')
    else:
        return 'Bad request'

