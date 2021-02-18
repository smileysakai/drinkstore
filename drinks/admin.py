from django.contrib import admin

from .models import Drink, Beverage

# Register your models here.
admin.site.register(Drink)
admin.site.register(Beverage)