from typing import ValuesView
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('word', views.word, name='word')   
]