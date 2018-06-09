#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 termninja <nmicovic@outlook.com>
#
# Distributed under terms of the MIT license.

import generate, sys

if len(sys.argv) != 2:
    sys.exit("Please supply a weights file as argument.")

model = generate.GenerativeNetwork('../epic_songs.txt', '../network/model.yaml', sys.argv[1])
# seed = input('Gimme some text: ')

seed = ''
seed = model.make_seed(seed)
generated = model.generate(seed)
print(generated)
