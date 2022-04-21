from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from django.utils.datetime_safe import datetime


class Costumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, default=None)
    last_name = models.CharField(max_length=30, default=None)
    age = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=200, default=None)
    contacts = models.IntegerField(null=True)
    citizen = models.CharField(max_length=100, default=None)
    created_time = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return str(self.user) + " - " +self.first_name + " " +self.last_name