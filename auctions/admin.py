from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, listings, watchlist

# Register your models here.
class listingsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price")

admin.site.register(User, UserAdmin),
admin.site.register(listings, listingsAdmin)
admin.site.register(watchlist)