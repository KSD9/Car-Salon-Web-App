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
    path('users',                  views.view_all_users,            name='usrs'),
    path('logout/', auth_views.logout,  {'next_page': '/index'},                         name='logout'),


#Car Views

    path('car/create',             views.add_car,                   name="addCar"),
    path('car/details/<id>',       views.details_car,               name="addCar"),
    path('car/edit/<id>',          views.edit_car,                  name="editCar"),
    path('car/deleteConfirm/<id>', views.delete_car_confirmation,   name="deleteCarConfimr"),
    path('car/delete/<id>',        views.delete_car,                name="deleteCar"),
    path('car/index',              views.view_all_cars,             name="cars"),
    path('car/sell/<id>',          views.sell_car,                  name="sellCar"),
    path('car/sold',               views.view_all_sold_cars,        name="soldCars"),

    #Appointment Views
    path('appointment/create/<id>', views.create_appointment,       name="appCreate"),
    path('appointment/index',       views.view_all_appointments,    name="appIndex"),

    #Email Sendind View From App Index Page
    path('index/sendEmail',         views.receive_email_from_user,  name="mail"),

]
