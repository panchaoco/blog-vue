# -*- coding: utf-8 -*-
__author__ = 'panchao'

from django.conf.urls import url, include
from . import views
app_name = '[article]'
urlpatterns = [
  url(r'', views.getArticleData, name="indexs")
]
