# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

import os

from flask import Flask
from pony.orm import Database

db = Database()

db_file = os.path.join(os.getcwd(), "guazi.db")

db.bind('sqlite', db_file, create_db=True)

app = Flask(__name__)

from web import views, models

db.generate_mapping(create_tables=True)
