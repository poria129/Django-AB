from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Meal(models.Model):
    person = models.ForeignKey(User,on_delete=models.CASCADE)
    #calorie_goal = models.IntegerField(default=0)
    food = models.ForeignKey("Food", on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    meal_calorie = models.IntegerField(default=0)

    created_date = models.DateTimeField()
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.pk)

class Food(models.Model):
    name_calorie_unit = models.CharField(max_length=250)
    coefficient = models.IntegerField(default=0)

    def __str__(self):
        return self.name_calorie_unit
