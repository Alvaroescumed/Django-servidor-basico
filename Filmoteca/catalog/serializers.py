from rest_framework import serializers
from .models import Film, Serie

#creamos los serializers para cada modelo

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ['id', 'title', 'director', 'release_date', 'genre', 'seasons']

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'director', 'release_date', 'genre']
    