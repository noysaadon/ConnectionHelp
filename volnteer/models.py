from django.db import models


class Volnteer(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=700)
    name_company = models.CharField(max_length=50)
    mail_company = models.EmailField()
    phone_company = models.CharField(max_length=15)
    website = models.CharField(max_length=1000)
    type = models.CharField(max_length=30)


class Charity(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=700)
    name_company = models.CharField(max_length=50)
    mail_company = models.EmailField()
    phone_company = models.CharField(max_length=15)
    website = models.CharField(max_length=1000)
    type = models.CharField(max_length=30)