from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Ataque(models.Model):
    attack_name = models.CharField(max_length=45)
    attack_value = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.attack_name

    class Meta:
        ordering = ["attack_name"]


class Pokemon(models.Model):
    ataques = models.ManyToManyField(Ataque, verbose_name="ataques")
    pokemon_name = models.CharField(max_length=45)
    pokemon_type = models.CharField(max_length=45)
    pokemon_image = models.ImageField(upload_to="pokemones",null = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.pokemon_name

    class Meta:
        ordering = ["-created"]


