from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


# importo el modelo
from .models import Ataque,Pokemon


# Create your views here.

class CatalogoPokemon(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, id = 0):
        if (id > 0):
            pokemons = list(Pokemon.objects.filter(id = id).values())
            if len(pokemons) > 0:
                pokemon = pokemons[0]
                datos = {'message': "Success", 'movies': pokemon}
            else:
                datos = {'message': "poke not found..."}
            return JsonResponse(datos)
        pokemones = list(Pokemon.objects.values())
        if len(pokemones) > 0:
            datos = {'message': "Success", 'pokemons': pokemones}
        else:
            datos = {'message': "pokemons dont found :("}
        return JsonResponse(datos)




#clase para los ataques

class AtaquesPokemon(View):


    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, id = 0):
        if (id > 0):
            attacks = list(Ataque.objects.filter(id = id).values())
            if len(attacks) > 0:
                ataque = attacks[0]
                datos = {'message': "Success", 'attacks': ataque}
            else:
                datos = {'message': "ataque not found..."}
            return JsonResponse(datos)
        ataques = list(Ataque.objects.values())
        if len(ataques) > 0:
            datos = {'message': "Success", 'attacks': ataques}
        else:
            datos = {'message': "ataque dont found :("}
        return JsonResponse(datos)

