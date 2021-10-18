from django.urls import path, include

#from Pokemon.AppPrincipal.models import Ataque
from .views import AtaqueViewset, FantasmaViewset, HieloViewset, LuchaViewset, PrincipalPokemon, AtaquesPokemon, FuegoPokemon, DragonPokemon, DragonViewset, FuegoViewset, PsiquicoViewset, TierraViewset, AguaViewset, ElectricoViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('dragon', DragonViewset)
router.register('fuego', FuegoViewset)
router.register('tierra', TierraViewset)
router.register('agua', AguaViewset)
router.register('electrico', ElectricoViewset)
router.register('hielo', HieloViewset)
router.register('psiquico', PsiquicoViewset)
router.register('lucha', LuchaViewset)
router.register('fantasma', FantasmaViewset)

router.register('ataque', AtaqueViewset )


urlpatterns=[
    path('pokemons/', PrincipalPokemon.as_view(), name='pokemons'),
    path('pokemons/<int:id>', PrincipalPokemon.as_view(), name='pokemons_process'),
    path('attacks/', AtaquesPokemon.as_view(), name='attacks'),
    path('attacks/<int:id>', AtaquesPokemon.as_view(), name='attacks_process'),

    path('pokemons/fuego/', FuegoPokemon.as_view(), name='fuego'),
    path('pokemons/dragon/', DragonPokemon.as_view(), name='dragon'),
    #path con django rest framework
    path('', include(router.urls)),
]