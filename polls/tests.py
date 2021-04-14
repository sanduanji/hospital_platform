from django.test import TestCase

# Create your tests here.
# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from mongoengine import connect
from models import *
import time



def test():
    pats = Patient.objects[:]
    print(type(pats))
    name = "张三"
    pats = [obj for obj in pa  ]
    for i in pats:
        print(i.name)


test()
