from django.shortcuts import render
from serializers import *
from rest_framework import generics
# Create your views here.


class RecipeList(generics.ListAPIView):
    model = Recipe
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


class IngredientList(generics.ListAPIView):
    model = Ingredient
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()


class AddRecipe(generics.CreateAPIView):
    model = Recipe
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

# class GroceryList(generics.ListAPIView):
#     model = Grocery
#     serializer_class = GrocerySerializer
#     queryset = Grocery.objects.all()
#
# class PrintList(generics.ListAPIView):
#     model = Print
#     serializer_class = PrintSerializer
#     queryset = Print.objects.all()