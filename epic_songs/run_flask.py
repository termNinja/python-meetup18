#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 termninja <nmicovic@outlook.com>
#
# Distributed under terms of the MIT license.

# from flask import Flask
# import app
# from app import app

# the_app = Flask(__name__)
# print(the_app)

# if __name__ == '__main__':
   # the_app.run()

import os
from app import app

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
