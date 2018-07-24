from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

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
    description               = models.CharField(max_length = 300)


class Appointment(models.Model):
    objects                   = models.Manager()
    startDate                 = models.DateTimeField()
    userId                    = models.ForeignKey (User,on_delete=models.CASCADE , related_name="cars")
    carId                     = models.ForeignKey (CarAstMar,on_delete=models.CASCADE , related_name="users")


class SoldCars(models.Model):
    objects                   = models.Manager()
    carId                     = models.ForeignKey (CarAstMar,on_delete=models.CASCADE , related_name="cars")
    quantity                  = models.PositiveIntegerField()    