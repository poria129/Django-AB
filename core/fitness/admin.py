from django.contrib import admin
from .models import Meal, Food

# Register your models here.

class MealAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = 'empty'
    list_display = ('person', 'food', 'meal_calorie', 'created_date')

admin.site.register(Meal,MealAdmin)
admin.site.register(Food)