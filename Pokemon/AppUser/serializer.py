from django.db import models
from django.db.models import fields
from rest_framework import serializers
from AppUser.models import User

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'