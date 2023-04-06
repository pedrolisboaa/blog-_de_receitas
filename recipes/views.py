from django.shortcuts import render
from utils.factory import make_recipe



# Create your views here.

def index(request):


    return render(request, 'index.html', context={'recipes': [make_recipe() for _ in range(10)]} )


def recipes(request, id):
    return render(request, 'recipes.html')
