#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 termninja <nmicovic@outlook.com>
#
# Distributed under terms of the MIT license.

from flask import Flask

app = Flask(__name__)
app.config['TESTING'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

from app import routes
