from django.db import models

# Create your models here.
class Client(models.Model):
    id= models.IntegerField(primary_key=True, unique=True)
    account_type= models.CharField()
    email= models.EmailField(unique=True)
    active= models.BooleanField()
    

class Address(models.Model):
    id=models.BigIntegerField(primary_key=True, unique=True)
    street=models.CharField()
    zipcode=models.BigIntegerField()
    state=models.CharField()
    appt_num=models.IntegerField(null=True, blank=True)

class Video(models.Model):
    id=models.BigIntegerField(primary_key=True, unique=True)
    title=models.CharField()
    in_stock=models.BigIntegerField()
    rating=models.CharField()
 
class Store(models.Model):
    id=models.BigIntegerField(primary_key=True, unique=True)
    name=models.CharField()
    number_of_employees=models.BigIntegerField()
    rating=models.FloatField()
    owner=models.BigIntegerField()


class Person(models.Model):
    id=models.BigIntegerField(primary_key=True, unique=True)
    first_name=models.CharField()
    last_name=models.CharField()
    middle_init=models.CharField(default=None)
    age=models.IntegerField()




