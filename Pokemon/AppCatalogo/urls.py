from django.urls import path
from .views import CatalogoPokemon, AtaquesPokemon

urlpatterns=[
    path('pokemons/', CatalogoPokemon.as_view(), name='pokemons'),
    path('pokemons/<int:id>', CatalogoPokemon.as_view(), name='pekemons_process'),
    path('attacks/', AtaquesPokemon.as_view(), name='attacks'),
    path('attacks/<int:id>', AtaquesPokemon.as_view(), name='attacks_process'),
]