# Create your models here.
from django.db import models
from django.contrib import admin
from ckeditor.fields import RichTextField
from ..Authentication.models import Costumer
from django.db.models.fields import DateTimeField
from datetime import datetime


class Services(models.Model):
    name = models.CharField(max_length=40)
    discription = RichTextField(null=True)
    create_time = DateTimeField(blank=True, auto_now_add=True)
    last_used_time = DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Images(models.Model):
    number = models.ForeignKey(Services, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="service_images", max_length=256)

    def __unicode__(self):
        return self.images


class Comments(models.Model):
    comments_count = models.ForeignKey(Services, on_delete=models.CASCADE)
    author = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    message = models.CharField(max_length=256)
    comment_time = DateTimeField(auto_now_add=True, blank=True)

    @admin.display(
        boolean=True,
        ordering='create_time',
        description='Commented Person',
    )
    def __str__(self):
        return self.message
