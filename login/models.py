from django.db import models

class User(models.Model):

    def __str__(self):
         return self.username   
 
    username = models.CharField(max_length=10)
    fullname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)