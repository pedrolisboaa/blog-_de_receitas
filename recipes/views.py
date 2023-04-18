from django.shortcuts import render
from django.http import Http404
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

    if not recipe:
        raise Http404('Not Found 😒')
    
    return render(request, 'category.html', context={
        'recipes': recipe,
        'title': f'CATEGORY | {recipe.first().category.title}'
        })


def recipes(request, id):
    return render(request, 'recipes.html', context={'recipe': make_recipe()})
