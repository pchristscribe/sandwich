from django.urls import path
from sandwichapp.views import SandwichappView, IngredientsListView, SandwichGeneratorView

urlpatterns = [
    # sandwich/
    path('', SandwichappView.as_view(), name='sandwich'),
    # sandwich/ingredients/<str:ingredient_type>
    path('ingredients/<str:ingredient_type>', IngredientsListView.as_view(), name='ingredients_list'),
    #random sandwich generation
    path('random', SandwichGeneratorView.as_view(), name='sandwich_generator')
    path('menu', )
]