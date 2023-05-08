from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404
from .models import Recipe
from django.db.models import Q

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
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()
    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ),
        is_published=True
    ).order_by('-id')

    recipes = recipes.filter(is_published=True)

    return render(request, 'searchpage.html', {
        'page_title': f'Pesquisar por "{search_term} |"',
        'search_term': search_term,
        'recipes': recipes,
    })
