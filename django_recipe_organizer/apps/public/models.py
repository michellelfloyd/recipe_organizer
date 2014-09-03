from django.db import models

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    ingredients = models.ManyToManyField('Ingredient')
    categories = models.CharField(max_length=50)
    description = models.TextField()
    instructions = models.TextField()
    # photo = models.FilePathField()

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
