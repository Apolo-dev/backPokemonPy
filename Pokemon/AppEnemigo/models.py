from django.db import models
from AppPrincipal.models import Ataque, Pokemon


# Create your models here.

class Aghata(models.Model):
    pokemones = models.ManyToManyField(Pokemon, verbose_name='pokemones')
    ataques = models.ManyToManyField(Ataque, verbose_name='ataques')

class Tomas(models.Model):
    pokemones = models.ManyToManyField(Pokemon, verbose_name='pokemones')
    ataques = models.ManyToManyField(Ataque, verbose_name='ataques')

class Fabiola(models.Model):
    pokemones = models.ManyToManyField(Pokemon, verbose_name='pokemones')
    ataques = models.ManyToManyField(Ataque, verbose_name='ataques')

class Daniel(models.Model):
    pokemones = models.ManyToManyField(Pokemon, verbose_name='pokemones')
    ataques = models.ManyToManyField(Ataque, verbose_name='ataques')

class Gary(models.Model):
    pokemones = models.ManyToManyField(Pokemon, verbose_name='pokemones')
    ataques = models.ManyToManyField(Ataque, verbose_name='ataques')