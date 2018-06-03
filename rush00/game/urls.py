#from django.conf.urls import  url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.init, name="init"),
    path('worldmap/', views.worldmap, name="worldmap"),
    path('load/', views.load, name="load"),
    path('options/save/', views.save, name="save"),
    path('options/save_A/', views.save_A, name="save_A"),
    path('options/save_B/', views.save_B, name="save_B"),
    path('options/save_up/', views.save_up, name="save_up"),
    path('options/save_down/', views.save_down, name="save_down"),
    path('up/', views.up, name="up"),
    path('down/', views.down, name="down"),
    path('left/', views.left, name="left"),
    path('right/', views.right, name="right"),
    path('options/', views.options, name="options"),
    path('moviedex/', views.moviedex, name="moviedex"),
    path('moviedex_up/', views.moviedex_up, name="moviedex_up"),
    path('moviedex_down/', views.moviedex_down, name="moviedex_down"),
    path('moviedex/<str:moviemon>/', views.details, name="details"),
]
