from django import views
from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Ataque, Pokemon
##from django.db.models import F
from rest_framework import viewsets
from .serializers import PokemonSerializer

class DragonViewset(viewsets.ModelViewSet):
    queryset = Pokemon.objects.filter(type_pokemon = 'Dragon')
    serializer_class = PokemonSerializer

class FuegoViewset(viewsets.ModelViewSet):
    queryset = Pokemon.objects.filter(type_pokemon = 'Fuego')
    serializer_class = PokemonSerializer

class TierraViewset(viewsets.ModelViewSet):
    queryset = Pokemon.objects.filter(type_pokemon = 'Tierra')
    serializer_class = PokemonSerializer

class AguaViewset(viewsets.ModelViewSet):
    queryset = Pokemon.objects.filter(type_pokemon = 'Agua')
    serializer_class = PokemonSerializer

class ElectricoViewset(viewsets.ModelViewSet):
    queryset = Pokemon.objects.filter(type_pokemon = 'Electrico')
    serializer_class = PokemonSerializer

class HieloViewset(viewsets.ModelViewSet):
    queryset = Pokemon.objects.filter(type_pokemon = 'Hielo')
    serializer_class = PokemonSerializer

class PsiquicoViewset(viewsets.ModelViewSet):
    queryset = Pokemon.objects.filter(type_pokemon = 'Psiquico')
    serializer_class = PokemonSerializer

class LuchaViewset(viewsets.ModelViewSet):
    queryset = Pokemon.objects.filter(type_pokemon = 'Lucha')
    serializer_class = PokemonSerializer

class FantasmaViewset(viewsets.ModelViewSet):
    queryset = Pokemon.objects.filter(type_pokemon = 'Fantasma')
    serializer_class = PokemonSerializer

class VoladorViewset(viewsets.ModelViewSet):
    queryset = Pokemon.objects.filter(type_pokemon = 'Volador')
    serializer_class = PokemonSerializer





























class PrincipalPokemon(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request):
        pokemones = list(Pokemon.objects.values())
        tipos = [
            {
                "Fuego": list(Pokemon.objects.filter(tipe_pokemon='Fuego').values())
            }
        ]
        
        #print(ataquesPokemon)
        if len(pokemones) > 0 and len(tipos) > 0:
            datos = {
                'message': "Success",
                #'pokemons': pokemones,
                'tipos': tipos
                }
        else:
            datos = {
                'message': "pokemons not found :("
                }
        return JsonResponse(datos)




class AtaquesPokemon(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request):
        
        pokemones1 = list(Pokemon.objects.values())
        #fuegos = list(Pokemon.objects.filter(tipe_pokemon = 'Fuego'))
        ataquePoke1 = list(Ataque.objects.filter(pokemon__id = 1).values())
        ataquePoke2 = list(Ataque.objects.filter(pokemon__id = 2). values())
        ataquePoke3 = list(Ataque.objects.filter(pokemon__id = 3).values())
        ataquePoke4 = list(Ataque.objects.filter(pokemon__id = 4). values())
        ataquePoke5 = list(Ataque.objects.filter(pokemon__id = 5).values())
        ataquePoke6 = list(Ataque.objects.filter(pokemon__id = 6). values())
        ataquePoke7 = list(Ataque.objects.filter(pokemon__id = 7).values())
        ataquePoke8 = list(Ataque.objects.filter(pokemon__id = 8). values())

        #print(ataques)
        if len(pokemones1)>0:
            datos = {
                'message': "Success",
                'pokemons':pokemones1,
                'ataques': [
                    {
                        'attacks1': ataquePoke1
                    },
                    {
                        'attacks2': ataquePoke2
                    },
                    {
                        'attacks3': ataquePoke3,
                    },
                    {
                        'attacks4': ataquePoke4,
                    },
                    {
                        'attacks5': ataquePoke5,
                    },
                    {
                        'attacks6': ataquePoke6,
                    },
                    {
                        'attacks7': ataquePoke7,
                    },
                    {
                        'attacks8': ataquePoke8,
                    }
                ]
                
}
        else:
            datos = {
                'message': "attacks not found :("
                }
        return JsonResponse(datos)


class FuegoPokemon(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        fuego = list(Pokemon.objects.filter(tipe_pokemon ='Fuego').values())
        
        #print(ataquesPokemon)
        if len(fuego) > 0:
            datos = {
                'message': "Success",
                'pokemonFuego': fuego,
                }
        else:
            datos = {
                'message': "pokemons not found :("
                }
        return JsonResponse(datos)

class DragonPokemon(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        dragon = list(Pokemon.objects.filter(tipe_pokemon ='Dragon').values())
        ataqueAltaria = list(Ataque.objects.filter(pokemon__name_pokemon = 'Altaria').values())
        ataqueAerodactyl = list(Ataque.objects.filter(pokemon__name_pokemon = 'Aerodactyl').values())
        ataqueDragonite = list(Ataque.objects.filter(pokemon__name_pokemon = 'Dragonite').values())

        
        
        #print(ataquesPokemon)
        if len(dragon) > 0 and len(ataqueAltaria) > 0 and len(ataqueAerodactyl) > 0:
            datos = {
                'message': "Success",
                'pokemonDragon': dragon,
                'ataques': [
                    {'at' : ataqueAltaria},
                    {'at' : ataqueAerodactyl},
                    {'at' : ataqueDragonite},
                ],
                
                }
        else:
            datos = {
                'message': "pokemons not found :("
                }
        return JsonResponse(datos)