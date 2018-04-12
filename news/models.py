from django.db import models


# from django.contrib.auth.models import User


# Create your models here.

# post class only for press

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(null=True, blank=True)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    category = models.ForeignKey('news.Category', blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


# class only for Gallery
class Gallery (models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(null=True, blank=True)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    category = models.ForeignKey('news.Category', blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title









# class for Category

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
