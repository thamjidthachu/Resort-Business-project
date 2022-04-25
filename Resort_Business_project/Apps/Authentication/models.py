from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from ..Services.models import Comments
from django.contrib.auth.models import User



class Costumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=200, default=None)
    contacts = models.IntegerField(null=True)
    citizen = models.CharField(max_length=100, default=None)
    created_time = models.DateTimeField(blank=True, auto_now_add=True)
    comments = GenericRelation('Comments')

    def __str__(self):
        return str(self.user)
