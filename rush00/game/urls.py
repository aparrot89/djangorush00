#from django.conf.urls import  url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.init, name="init"),
    path('worldmap/', views.worldmap, name="worldmap"),
    path('load/', views.load, name="load"),
    path('up/', views.up, name="up"),
    path('down/', views.down, name="down"),
    path('left/', views.left, name="left"),
    path('right/', views.right, name="right"),
    path('start/', views.start, name="start"),
    path('select/', views.select, name="select"),
]
