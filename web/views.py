# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

from flask import render_template, request
from pony.orm import db_session, desc

from web import app
from web.models import Nut


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        with db_session:
            nuts = Nut.select().order_by(desc(Nut.datetime))
            return render_template("index.html", nuts=nuts)
    elif request.method == "POST":
        pass
