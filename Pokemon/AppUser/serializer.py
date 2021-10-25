from django.db import models
from django.db.models import fields
from rest_framework import serializers
from AppUser.models import User

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name')

# serializador para guardar
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

# serializador para listar

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        