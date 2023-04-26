from django.urls import path, include
from .views import index, recipes, category


app_name = 'recipes'

urlpatterns = [
    path('', index, name='home'),
    path('recipes/<int:id>/', recipes, name='recipe'),
    path('recipes/category/<int:category_id>/', category, name='category'),
]
