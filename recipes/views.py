from django.shortcuts import render, get_list_or_404
from utils.recipes.main import make_recipe
from .models import Recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    context = {"recipes": recipes, }
    return render(request, 'recipes/pages/home.html',
                  context=context)


def recipes(request, id):
    # Tenta recuperar a receita pelo ID ou retorna 404 se não for encontrada
    recipe = Recipe.objects.filter(id=id).first()
    # Define o contexto com a receita recuperada
    context = {
        'recipe': recipe,
        'title': f'{recipe.title}'
    }

    # Renderiza o template com o contexto da receita
    return render(request, 'recipes/pages/recipe-view.html', context)


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id, is_published=True).order_by('-id'))

    # Define o contexto para passar para o template
    context = {
        'recipes': recipes,
        'title': f"{recipes[0].category.name}"
    }

    # Renderiza o template com o contexto
    return render(request, 'recipes/pages/category.html', context)

