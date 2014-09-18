from models import *
from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = serializers.SerializerMethodField('get_ingredients')
    class Meta:
        model = Recipe

    def get_ingredients(self, obj):
        return IngredientSerializer(obj.ingredients.all(), many=True).data


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient


# class GrocerySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Grocery
#
#
# class PrintSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Print