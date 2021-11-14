from django.contrib import admin
from .models import User, Restaurant, FoodsAndCategories, Order

class Admin(admin.ModelAdmin):
    filter_horizontal = {'Users'}

admin.site.register(User)
admin.site.register(FoodsAndCategories)
admin.site.register(Restaurant)
admin.site.register(Order)