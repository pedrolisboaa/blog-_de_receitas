from django.shortcuts import render
from utils.factory import make_recipe
from .models import Recipe



# Create your views here.

def index(request):
    
    recipes = Recipe.objects.filter(
       is_published=True
       ).order_by('-id')
    
    
    return render(request, 'index.html', context={'recipes': recipes} )


def category(request, category_id):
    
    recipe = Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
        ).order_by('-id')
    
    
    return render(request, 'category.html', context={'recipes': recipe} )


def recipes(request, id):
    return render(request, 'recipes.html', context={'recipe': make_recipe()})
