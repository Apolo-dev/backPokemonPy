from django.urls import path

#from Pokemon.AppPrincipal.models import Ataque
from .views import PrincipalPokemon, AtaquesPokemon, FuegoPokemon, DragonPokemon

urlpatterns=[
    path('pokemons/', PrincipalPokemon.as_view(), name='pokemons'),
    path('pokemons/<int:id>', PrincipalPokemon.as_view(), name='pokemons_process'),
    path('attacks/', AtaquesPokemon.as_view(), name='attacks'),
    path('attacks/<int:id>', AtaquesPokemon.as_view(), name='attacks_process'),

    path('pokemons/fuego/', FuegoPokemon.as_view(), name='fuego'),
    path('pokemons/dragon/', DragonPokemon.as_view(), name='dragon'),
]