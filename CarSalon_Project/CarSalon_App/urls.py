from django.urls import path
from CarSalon_App import views
from django.contrib.auth import views as auth_views

urlpatterns = [
# App Entry Urls
    path('',                       views.application_index,         name='appIndex'),
    path('index',                  views.application_index,         name ="index"),

#Auth Views

    path('login/',                 auth_views.login, {'template_name': 'CarSalon_App/auth/login.html'},  name='login'),
    path('register/',              views.register,                  name='login'),
    path('viewUsers',              views.view_all_users,            name='usrs'),


#Car Views

    path('car/create',             views.add_car,                   name="addCar"),
    path('car/details/<id>',       views.details_car,               name="addCar"),
    path('car/edit/<id>',          views.edit_car,                  name="editCar"),
    path('car/deleteConfirm/<id>', views.delete_car_confirmation,   name="deleteCarConfimr"),
    path('car/delete/<id>',        views.delete_car,                name="deleteCar"),
    path('car/index',              views.view_all_cars,             name="cars")
]