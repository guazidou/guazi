# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

from datetime import datetime

from pony.orm import Required, PrimaryKey

from web import db


class Nut(db.Entity):
    id = PrimaryKey(int, auto=True)
    context = Required(str)
    datetime = Required(datetime)
    author = Required(str)


    def get_datatime(self):
        return self.datetime.strftime("%Y-%m-%d %H:%M:%S")
