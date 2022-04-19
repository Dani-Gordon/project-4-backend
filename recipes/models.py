from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name       

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200, null=True)
    prep = models.IntegerField(null=True)
    total = models.IntegerField(null=True)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredients')
    directions = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.name 

class RecipeIngredients(models.Model):
    recipetitle = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.recipetitle.name} {self.ingredient.name} {self.quantity}'


