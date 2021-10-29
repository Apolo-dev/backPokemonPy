
from .models import Pokemon
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

class LegendarioViewset(viewsets.ModelViewSet):
    queryset = Pokemon.objects.filter(type_pokemon = 'Legendario')
    serializer_class = PokemonSerializer
