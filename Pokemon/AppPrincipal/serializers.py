from .models import Ataque, Pokemon
from rest_framework import serializers

class AtaqueSerializer(serializers.ModelField):
    class Meta:
        model = Ataque
        fields = '__all__'

class PokemonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
        fields = '__all__'

    
