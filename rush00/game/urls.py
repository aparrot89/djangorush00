#from django.conf.urls import  url
from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.init, name="init"),
    path('coucou/', views.coucou, name="coucou"),
]
