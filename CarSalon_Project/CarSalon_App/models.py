from django.db import models
from datetime import datetime
from django.contrib.auth.models import User , AbstractUser



user_roles = (
('RentManager','Rent Manager'),
('SalesManager','Sales Manager'),
('Administrator','Administrator'),
('SuperUser','Super User')

)
class MyUser(AbstractUser):
    role  = models.CharField(max_length = 300, choices = user_roles )
    image = models.ImageField(upload_to = 'uploaded/') #default ='image')        

class CarAstMar(models.Model):
    objects                   = models.Manager()
    model                     = models.CharField(max_length = 200)
    year                      = models.PositiveIntegerField()
    color                     = models.CharField(max_length = 50)
    price                     = models.PositiveIntegerField()
    quantity                  = models.PositiveIntegerField()
    horsePowers               = models.PositiveIntegerField()
    engineType                = models.CharField(max_length = 200)
    topSpeed                  = models.PositiveIntegerField()
    zeroToHundredAcceleration = models.PositiveIntegerField()
    image                     = models.ImageField()
    isForRent                 = models.BooleanField(default = False)
    isRented                  = models.BooleanField(default = False)
    description               = models.CharField(max_length = 300)


class Appointment(models.Model):
    objects                   = models.Manager()
    startDate                 = models.DateTimeField()
    userId                    = models.ForeignKey (MyUser,on_delete=models.CASCADE , related_name="usersApp")
    carId                     = models.ForeignKey (CarAstMar,on_delete=models.CASCADE , related_name="carsApp")


class SoldCars(models.Model):
    objects                   = models.Manager()
    carId                     = models.ForeignKey (CarAstMar,on_delete=models.CASCADE , related_name="carsSold")
    quantity                  = models.PositiveIntegerField()
    date                      = models.DateTimeField()
    employeId                 = models.ForeignKey (MyUser,on_delete=models.CASCADE , related_name="soldCarUser")
    

class SystemLog(models.Model):
    objects                   = models.Manager()
    userId                    = models.ForeignKey (MyUser,on_delete=models.CASCADE , related_name="usersSysLog")
    action                    = models.CharField(max_length = 300)
    dateTime                  = models.DateTimeField()
    model                     = models.CharField(max_length = 300)

class RentedCars(models.Model):
    objects                   = models.Manager()
    carId                     = models.ForeignKey (CarAstMar,on_delete=models.CASCADE , related_name="carsRented")
    startDate                 = models.DateField()
    endDate                   = models.DateField()
    employeId                 = models.ForeignKey (MyUser,on_delete=models.CASCADE , related_name="rentCarUser")
