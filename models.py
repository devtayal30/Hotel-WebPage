from django.db import models

class RoomAvailability(models.Model):
    AC_Room=models.CharField(max_length=100)
    Non_AC_Room= models.CharField(max_length=100)

# Create your models here.
