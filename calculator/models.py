from django.db import models

class CalorieData(models.Model):
    date = models.DateField()
    calories_consumed = models.IntegerField()
    goal_calories = models.IntegerField()