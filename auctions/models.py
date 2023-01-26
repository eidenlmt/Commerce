from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class listings(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=256, default='Description')
    created_on = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='auctions/files/images', default='Photo', blank=True)

class bids():
    pass

class comments():
    pass

class watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(listings, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user} watchlist"