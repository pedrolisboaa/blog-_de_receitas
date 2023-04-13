from django.urls import path, include
from .views import index, recipes


app_name = 'recipes'

urlpatterns = [
    path('', index, name='home'),
    path('recipes/<int:id>/', recipes, name='recipe'),
]