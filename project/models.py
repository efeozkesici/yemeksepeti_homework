from django.db import models

class User(models.Model):
    nameSurname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.email}"

class Restaurant(models.Model):
    restaurantName = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.restaurantName}"

class FoodsAndCategories(models.Model):
    foodName = models.CharField(max_length=100)
    categoryName = models.CharField(max_length=100)
    restaurant = models.ManyToManyField(Restaurant, related_name='foodsAndCategories')

    def __str__(self):
        return f"{self.foodName}_{self.categoryName}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    foodName = models.CharField(max_length=100)
    categoryName = models.CharField(max_length=100)
    restaurant = models.CharField(max_length=100)
    orderStatus = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user}_{self.foodName}_{self.categoryName}_{self.restaurant}"


