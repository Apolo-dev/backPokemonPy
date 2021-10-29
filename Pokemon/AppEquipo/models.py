from django.db import models

from AppPrincipal.models import Ataque, Pokemon
from AppUser.models import User

# Create your models here.

class Equipo(models.Model):
    pokemones = models.ManyToManyField(Pokemon, verbose_name='pokemones')
    usuarios = models.ForeignKey(User, on_delete=models.CASCADE)
    

