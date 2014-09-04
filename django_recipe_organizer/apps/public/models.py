from django.db import models

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    ingredients = models.ManyToManyField('Ingredient')
    description = models.TextField(default="No description has been entered yet")
    instructions = models.TextField(default="No instructions have been entered yet")
    categories = models.CharField(max_length=50)
    photo = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.name


# class Quantity(models.Model):
#     amount = models.ManyToManyField('Ingredient')
#
#     def __unicode__(self):
#         return self.name
#
#

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name



# class Grocery(models.Model):
#     name = models.ManyToManyField('Ingredient')
#     amount = models.ManyToManyField('Quantity')
#
#     def __unicode__(self):
#         return self.name
#
#
# class Print(models.Model):
#     pass
