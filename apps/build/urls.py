'''
Created on 9 Apr 2009

@author: dalore
'''

from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^version/?$', direct_to_template, {"template": "VERSION.txt"}, name="version"),
)