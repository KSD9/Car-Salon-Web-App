from django.urls import path
from CarSalon_App import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # App Entry Urls
    path('',  views.application_index,     name='appIndex'),
    path('index', views.application_index,  name ="index"),
]