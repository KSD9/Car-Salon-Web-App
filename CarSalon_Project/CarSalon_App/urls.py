from django.urls import path
from CarSalon_App import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # App Entry Urls
    path('',  views.application_index,     name='appIndex'),
    path('index', views.application_index,  name ="index"),
    path('login/', auth_views.login, {'template_name': 'CarSalon_App/auth/login.html'}, name='login'),
    path('register/', views.register, name='login'),
    path('viewUsers',views.view_all_users,name='usrs')
]
