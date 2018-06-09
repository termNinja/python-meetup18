#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 termninja <nmicovic@outlook.com>
#
# Distributed under terms of the MIT license.

import sys
import network.generate as generate

model = generate.GenerativeNetwork('./epic_songs.txt', 'network/model.yaml', 'network/weights-74-0.595.hdf5')

def predict(seed=''):
    # seed = seed.encode('ascii', 'ignore')
    # seed = 'само јуначки'
    print('fseed {}'.format(seed))
    print('type {}'.format(type(seed)))
    # seed = seed.decode(seed, 'utf-8', errors='ignore')
    seed = seed.encode('utf8')
    # seed = unicode(seed, 'utf-8', errors='ignore')
    seed = model.make_seed(seed)
    generated = model.generate(seed)
    print('generated {}'.format(generated))
    generated = unicode(generated, 'utf-8', errors='ignore')
    return generated
