from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.public.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recipe_organizer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^recipes/$', RecipeList.as_view(), name='recipe-list'),
    url(r'^ingredients/$', IngredientList.as_view(), name='ingredient-list'),
    # url(r'^grocery/$', GroceryList.as_view(), name='grocery-list'),
    # url(r'^print/$', PrintList.as_view(), name='print-list'),


)
