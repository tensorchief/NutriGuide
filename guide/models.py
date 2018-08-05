from django.db import models
from django.contrib.auth.models import User

import datetime


# Create your models here.
class TitleCard(object):

    def __init__(self, title, description, colour, icon):
        self.icon = icon
        self.colour = colour
        self.title = title
        self.description = description


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    sex = models.CharField(
        max_length=1,
        choices=(
            ('M', 'Male'),
            ('F', 'Female')
        )
    )
    date_of_birth = models.DateField()
    weight = models.DecimalField(
        'weight (kg)',
        max_digits=5,
        decimal_places=2
    )
    height = models.DecimalField(
        'height (cm)',
        max_digits=5,
        decimal_places=2
    )
    # TODO: goal (gains, weight loss etc)

    def age(self):
        return (datetime.date.today() - self.date_of_birth) // datetime.timedelta(days=365.2425)


class NutritionGoal(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    calories = models.IntegerField()
    carbohydrates = models.IntegerField()
    proteins = models.IntegerField()
    fats = models.IntegerField()


class Recipe(models.Model):
    name = models.CharField(
        max_length=100
    )
    description = models.TextField()
    duration = models.DurationField()
    difficulty = models.SmallIntegerField(
        choices=(
            (1, 'easy'),
            (2, 'medium'),
            (3, 'hard')
        )
    )
    calories = models.IntegerField()
    carbohydrates = models.IntegerField()
    proteins = models.IntegerField()
    fats = models.IntegerField()
    source = models.URLField()


class Meal(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE
    )
    amount = models.SmallIntegerField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    date = models.DateField()
    meal = models.SmallIntegerField(
        choices=(
            (1, 'Breakfast'),
            (2, 'Lunch'),
            (3, 'Dinner'),
            (4, 'Snack')
        )
    )


class PreparationStep(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE
    )
    step = models.IntegerField()
    description = models.TextField()


class Ingredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=50
    )
    amount = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    unit = models.CharField(
        max_length=50
    )
