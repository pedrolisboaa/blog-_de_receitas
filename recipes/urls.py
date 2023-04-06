from django.urls import path, include
from .views import index, recipes

urlpatterns = [
    path('', index, name='index'),
    path('recipes/<int:id>/', recipes, name='recipes'),
]