from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class Car(models.Model):
    number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.number


class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateTimeField(null=True)
    cars = models.ManyToManyField(Car, through='Ownership')
    passport = models.IntegerField(max_length=10)
    address = models.CharField(max_length=60)
    nationality = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=16, unique=True)
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Ownership(models.Model):
    User = get_user_model()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.owner} - {self.car}"


class DriverLicense(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date = models.DateTimeField

