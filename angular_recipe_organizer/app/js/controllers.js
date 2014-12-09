'use strict';

/* Controllers */

angular.module('myApp.controllers', [])
    .controller('RecipeCtrl', ['$scope', 'Restangular', function ($scope, Restangular) {

        // GET a list of all recipes
        Restangular.all('recipes/‘).getList().then(function (recipes) {
            $scope.recipes = recipes;
        })
    }])


    .controller('AddRecipeCtrl', ['$scope', 'Restangular', function ($scope, Restangular) {

        $scope.searchTerm = "";

        $scope.addIngredient = function () {
            $scope.createNewIngredient = true;
        };
        $scope.saveIngredient = function (name) {
            //Ensure no duplicate entries

            if (ingredientExists(name)) {
                $scope.newIngredient.$error = true;
                return;
            }
            $scope.createNewIngredient = false;
            var obj = {
                name: name
            };
            Restangular.all('ingredients/').customPOST(obj).then(function (ingredient) {
                $scope.ingredients.push(ingredient);
                $scope.newIngredient = {};
            });
        };

        $scope.cancelIngredient = function () {
            $scope.newIngredient = {};
            $scope.createNewIngredient = false;
        };

        var ingredientExists = function (name) {
            for (var i = 0; i < $scope.ingredients.length; i++) {
                if (name.toLowerCase() === $scope.ingredients[i].name.toLowerCase()) {
                    return true;
                }
            }
            return false;
        };

        Restangular.all('ingredients/‘).getList().then(function (ingredients) {
            $scope.ingredients = ingredients;
        });

        $scope.recipe = { ingredients: []};

        $scope.addRecipe = function () {
            for (var i in $scope.recipe.ingredients) {
                var ing = $scope.recipe.ingredients[i];
                $scope.recipe.ingredients[i] = ing.id;
            }
            Restangular.all('add-recipe/').customPOST($scope.recipe).then(function () {
                alert("Your recipe was successfully added!");
                $scope.recipe = { ingredients: []};
            }, function () {
                alert("There was a problem adding your recipe.");
            });
        };
    }])



    .controller('RecipeDetailCtrl', ['$scope', 'Restangular', '$routeParams', function ($scope, Restangular, $routeParams) {
        $scope.editing = false;
        var recipeId = $routeParams.id;
        // GET a list of all recipes
        Restangular.one('recipes/‘, recipeId).get().then(function (recipe) {
            $scope.recipe = recipe;
        });
        $scope.saveRecipe = function () {
            $scope.recipe.put();
            $scope.editing = false
        }


    }])


    .controller('EditRecipeCtrl', function ($scope, Restangular, $routeParams, $location) {
        $scope.recipeId = $routeParams.recipeId;

        Restangular.one('recipes/‘, $scope.recipeId).customGET().then(function (data) {
//            data.ingredient_ids = [];
//            for (var i=0; i<data.ingredients.length; i++){
//                data.ingredient_ids.push(data.ingredients[i].id);
//            }
//            data.ingredients = data.ingredient_ids;
            $scope.recipe = data;

        });
//        Restangular.all('ingredients/‘).getList().then(function (ingredients) {
//            $scope.ingredients = ingredients;
//        });

        $scope.updateRecipe = function () {
            Restangular.one('recipes/‘, $scope.recipeId).customPUT($scope.recipe).then(function (data) {
                    $scope.status = "The recipe was successfully edited!";
                    $scope.recipe = data;
                    $location.path('/recipes');
                }, function () {
                    $scope.status = "The recipe couldn't be saved";
                }
            )
        };

        $scope.deleteRecipe = function() {
            if (confirm("Are you sure you want to delete this recipe?")) {
                Restangular.one('recipes/‘, $scope.recipeId).customDELETE().then(function (data) {
                    $location.path('/recipes');
                }, function() {
                    $scope.status = "The recipe couldn't be deleted";
                });
            }

        };
    });