from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Recipe


# Create your views here.

def index(request):
    recipes = Recipe.objects.filter(
        is_published=True,
    ).order_by('-id')

    return render(request, 'index.html', context={'recipes': recipes})


def category(request, category_id):
    recipe = get_list_or_404(Recipe, category__id=category_id, is_published=True)  # noqa: E501
    return render(request, 'category.html', context={
        'recipes': recipe,
        'title': f'CATEGORY | {recipe[0].category.title}'
        })


def recipes(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)

    return render(request, 'recipes.html', context={
        'recipe': recipe,
        'is_detail_page': True,
        })


def search(request):
    search_term = request.GET.get('q')

    return render(request, 'searchpage.html')
