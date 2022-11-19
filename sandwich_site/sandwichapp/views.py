from django.shortcuts import render
from django.http import Http404
from django.views import View
import random

ingredients = {
    'meats': ['corned beef', 'pastrami', 'meatballs', 'capicola', 'beyond burger', 'roast pork'],
    'cheeses': ['american', 'swiss', 'provolone', 'cheddar', 'mozzarella', 'muenster'],
    'toppings': ['lettuce', 'roma tomato', 'onions', 'italian long hots', 'pickles', 'broccoli rabe']
}

class SandwichappView(View):
    def get(self, request):
        return render(
            request = request,
            template_name = 'sandwichapp.html',
            context = {'ingredients': ingredients.keys()}
        )

class IngredientsListView(View):
    def get(self, request, ingredient_type):
        if ingredient_type not in ingredients:
            raise Http404(f'No such ingredient: {ingredient_type}')
        return render(
            request = request,
            template_name = 'ingredients_list.html',
            context= {
                'ingredients': ingredients[ingredient_type],
                'ingredient_type': ingredient_type,
            }
        )
class SandwichGeneratorView(View):
    def get(self, request):
            selected_meat = random.choice(ingredients['meats'])
            selected_cheese = random.choice(ingredients['cheeses'])
            selected_toppings = random.choice(ingredients['toppings'])

            sandwich = f'{selected_meat} & {selected_cheese} with {selected_toppings}'
            return render(
                request, 
                template_name ='sandwich_generator.html',
                context = { 'sandwich' : sandwich}
                )
class MenuGeneratorView(View):
    def get(self, request):
        return render(
            request, 
            template_name = "menu_generator.html",
            context={
                "meats": ingredients["meats"],
                "cheeses": ingredients["cheeses"],
                "toppings": ingredients["toppings"]})