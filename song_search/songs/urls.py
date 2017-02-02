from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'search/', views.search_songs),
    url(r'manage/', views.manage),
    url(r'details/', views.details),
]
