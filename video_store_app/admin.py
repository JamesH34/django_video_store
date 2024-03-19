from django.contrib import admin

# Register your models here.
from .models import Client, Address, Video, Store, Person

admin.site.register([Client, Address, Video, Store, Person])