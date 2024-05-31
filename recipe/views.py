from django.shortcuts import render

# Create your views here.
from .models import Recipe


def main_view(request):
    recipes_2023 = Recipe.objects.filter(year=2023)
    return render(request, 'main.html', {'recipes': recipes_2023})


def recipe_detail_view(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})
