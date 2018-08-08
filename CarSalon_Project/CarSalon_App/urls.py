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
    path('logout/',                auth_views.logout,  {'next_page': '/index'},                          name='logout'),

#Car Views
    path('car/create',             views.add_car,                   name="addCar"),
    path('car/details/<id>',       views.details_car,               name="addCar"),
    path('car/edit/<id>',          views.edit_car,                  name="editCar"),
    path('car/deleteConfirm/<id>', views.delete_car_confirmation,   name="deleteCarConfimr"),
    path('car/delete/<id>',        views.delete_car,                name="deleteCar"),
    path('car/index',              views.view_all_cars,             name="cars"),
    path('car/sell/<id>',          views.sell_car,                  name="sellCar"),
    path('car/sold',               views.view_all_sold_cars,        name="soldCars"),

# Rent Cars Views
    path('car/rent/create',        views.create_car_for_rent ,      name="rentCar"),
    path('car/rent/edit/<id>',     views.edit_car_for_rent,         name="editRentedCar"),
    path('car/rent/index',         views.rent_cars_index,           name="rentedCars"),
    path('car/rent/delete/<id>',   views.delete_rent_car,           name="rentedCars"),

# Sell Cars Views    
    path('car/sll/index',         views.sell_car_index,             name="sellCars"),
    path('car/sell/request/<id>',  views.sell_car_request,           name="sellCars"),
    path('car/request', views.index_sell_car_request,           name="sellCars"),


#Appointment Views
    path('appointment/create/<id>', views.create_appointment,       name="appCreate"),
    path('appointment/index',       views.view_all_appointments,    name="appIndex"),

#Email Sendind View From App Index Page
    path('index/sendEmail',         views.receive_email_from_user,  name="mail"),
    path('admin/',                  views.back_office_index),

#Users Views
    path('user/index', views.users_index,name="users"),
     path('user/edit/<id>', views.show_user,name="editUSer"),
     path('usr/edit/<id>',views.edit_user,name="asd"),
    path('sysLog/index', views.system_log_index , name="logs")

]

