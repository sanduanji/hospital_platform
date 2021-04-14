from django.db import models

# Create your models here.
import mongoengine
from django.db import models
from django import forms
from django.forms import fields,widgets
from mongoengine import connect
connect('hulian', host='127.0.0.1', port =27017)




class Zhenduan03(mongoengine.Document):
    _id = mongoengine.StringField()
    name = mongoengine.StringField()
    hospital = mongoengine.StringField()
    id = mongoengine.StringField()
    menzhenhao = mongoengine.StringField()
    jilushijian = mongoengine.StringField()
    minzu = mongoengine.StringField()
    hunyin = mongoengine.StringField()
    zhiye = mongoengine.StringField()
    shengri = mongoengine.StringField()
    chushengdi = mongoengine.StringField()
    jiguandi = mongoengine.StringField()
    bingshichenshu = mongoengine.StringField()
    yongyaolishi = mongoengine.StringField()
    zhusu = mongoengine.StringField()
    tigejiancha = mongoengine.StringField()
    chubuzhenduan = mongoengine.StringField()
    chuli = mongoengine.StringField()
    age = mongoengine.StringField()
    keshi = mongoengine.StringField()
    gender = mongoengine.StringField()
    meta = {'collection':'zhenduan_vthree'}


def testconnect():
    pname = '张美'
    pid = '310110198101021801'
    reports = Zhenduan03.objects(name = pname, id = pid)
    print(reports)

testconnect()
