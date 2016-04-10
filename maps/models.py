from __future__ import unicode_literals
from django.db import models
from mongoengine import *

# Create your models here.

class Loc(EmbeddedDocument):
    type = StringField()
    coordinates = ListField(FloatField())

class Post(Document):
    meta = {
        'collection': 'posts',
        'allow_inheritance': False,
        'strict': False
    }
    gps_num = IntField()
    app = StringField()
    s_d1 = FloatField()
    date = DateTimeField()
    s_d0 = FloatField()
    gps_alt = IntField()
    s_h0 = FloatField()
    gps_fix = IntField()
    ver_app = FloatField()
    device_id = StringField()
    s_t0 = FloatField()
    device = StringField()
    tick = IntField()
    s_4 = FloatField()
    s_1 = FloatField()
    s_0 = FloatField()
    s_3 = FloatField()
    s_2 = FloatField()
    ver_format = IntField()
    FAKE_GPS = IntField()
    time = DateTimeField()
    loc = PointField()
    fmt_opt = IntField()


