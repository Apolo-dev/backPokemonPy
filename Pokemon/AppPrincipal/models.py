from django.db import models

# Create your models here.

class Ataque(models.Model):
    
    name_attack = models.CharField(max_length=50)
    type_attack = models.CharField(max_length=40)
    value_attack = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name_attack

    class Meta:
        ordering = ['name_attack']

class Pokemon(models.Model):
    ataques = models.ManyToManyField(Ataque, verbose_name='ataques')
    name_pokemon = models.CharField(max_length=45)
    type_pokemon = models.CharField(max_length=45)
    image_pokemon = models.ImageField(upload_to="pokemones",null = True)
    life_pokemon = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name_pokemon

    class Meta:
        ordering = ['name_pokemon']



