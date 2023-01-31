from django.contrib.auth.models import AbstractUser
from django.db import models

# Categories
CATEGORIES = [
    ('misc', 'misc'),
    ('computers','computers'),
    ('toys','toys'),
    ('pets','pets'),
    ('beauty','beauty'),
    ('video games','video games'),
    ('food','food'),
    ('clothing','clothing'),
]

class User(AbstractUser):
    pass

class listings(models.Model):
    title = models.CharField(max_length=64, default='Title')
    description = models.TextField(max_length=256, default='Description')
    category = models.CharField(max_length=30, choices=CATEGORIES, default='misc')
    created_on = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default='Starting Price')
    image = models.ImageField(upload_to='auctions/files/images', default='Photo', blank=True)

class bids(models.Model):
    bids = models.DecimalField(max_digits=8, decimal_places=2 , default='Bid')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class comments(models.Model):
    pass

class watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(listings, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user} watchlist"