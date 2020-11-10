"""
#from django.db import models
from firebase_orm import models



# Create your models here.

class Register(models.Model):
    name = models.TextField()
    contact = models.TextField()
    username = models.TextField()
    password = models.TextField()

    class Meta:
        db_table = 'Registration'

    def __str__(self):
        return self.name



"""