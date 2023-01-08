from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class listings(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=256, default='Description')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='auctions/files/images', default='Photo', blank=True)

class bids():
    pass

class comments():
    pass