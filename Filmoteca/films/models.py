from django.db import models

#Creamos nuestros dos modelos Actor y Films

class Actor(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Film(models.Model):

    title = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor, related_name='films')
    release_date = models.DateField()
    genre = models.CharField(max_length=100)

    # retornamos el titulo del objeyto pelicula
    def __str__(self):
        return self.title

