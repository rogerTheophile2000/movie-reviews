from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('addNews', views.createNews, name='addNews'),
]
