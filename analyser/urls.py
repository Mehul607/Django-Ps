from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^analysed/', views.mainS, name='an_main'),
    url(r'^$', views.main, name='main'),
]