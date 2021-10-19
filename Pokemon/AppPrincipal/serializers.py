from django.db import models
from django.db.models import fields
from .models import Ataque, Pokemon
from rest_framework import serializers

class AtaqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ataque
        fields = '__all__'

class PokemonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pokemon
        fields = '__all__'