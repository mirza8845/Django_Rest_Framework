from random import choices

from Cryptodome.Random.random import choice
from django.db import models

# Create your models here.
# Create Company Model

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField(max_length=100)
    type = models.CharField(max_length=100, choices=(('IT', 'IT'), ('None IT', 'None IT'), ('Tech', 'Tech')))
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    about = models.TextField(max_length=100)
    position = models.CharField(max_length=100, choices=(('Manager', 'manager'), ('Software Developer', 'sd'), ('Project Lead', 'pl')))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Places(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)