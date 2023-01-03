from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Fit(models.Model):
    '''
    This is a class to define fit for fitness app.
    '''
    person = models.ForeignKey(User,on_delete=models.CASCADE)
    meal = models.ForeignKey('meal', on_delete=models.SET_NULL,null=True)
    sum_today_calories = models.IntegerField(default=0)
    calculated_calories = models.IntegerField(default=0)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class Meal(models.Model):
    food = models.ForeignKey('food', on_delete=models.SET_NULL,null=True)
    amount = models.IntegerField(default=0)
    calorie = models.IntegerField(default=0)

class Food(models.Model):
    name = models.CharField(max_length=250)
    unit_calorie = models.IntegerField(default=0)

