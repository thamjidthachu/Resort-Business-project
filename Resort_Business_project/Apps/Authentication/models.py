from django.contrib.auth.models import User
from django.db import models


class Costumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=200, default=None)
    contacts = models.IntegerField(null=True)
    citizen = models.CharField(max_length=100, default=None)
    created_time = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return str(self.user)
