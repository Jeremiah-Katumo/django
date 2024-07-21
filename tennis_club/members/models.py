from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    # To change the string representation, we have to define the __str__() function of the Member Model in models.py
    def __str__(self):
        return f"{self.firstname} {self.lastname}"