from django.contrib.auth.models import AbstractUser
from django.db import models

from users.validators import not_rambler


class Location(models.Model):
    name = models.CharField(max_length=200)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.name


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    birth_date = models.DateField(null=True)
    email = models.EmailField(validators=[not_rambler], unique=True)
    location = models.ManyToManyField(Location, blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

