from django.db import models

#Creamos nuestros dos modelos Actor y Films

class Serie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    seasons= models.IntegerField()

class Film(models.Model):

    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)

    # retornamos el titulo del objeyto pelicula
    def __str__(self):
        return self.title

