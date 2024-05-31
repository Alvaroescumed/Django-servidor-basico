from django.db import models

# Creamos un modelo generico del producto ya que tento serie como pelicula comparten muchos campos

class ProductBase(models.Model):

    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)

    # Añadimos que es abstracto para que no se genere como una tabla en la BD
    class Meta: 
        abstract = True

    # retornamos el titulo del objeto
    def __str__(self):
        return self.title

# Creamos los modelos a partir del base

class Film(ProductBase):
    pass


class Serie(ProductBase):

    #Integramos el campo de 'seasons' en el modelo de serie ya que la base no la incluye
    seasons = models.IntegerField()
