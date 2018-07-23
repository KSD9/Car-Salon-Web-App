from django.db import models

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
    description               = models.CharField(max_length = 300)
