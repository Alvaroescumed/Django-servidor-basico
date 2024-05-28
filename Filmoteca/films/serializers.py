from rest_framework import serializers
from .models import Film, Serie

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ['id', 'title', 'actors', 'release_date', 'genre', 'seasons']

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'director', 'release_date', 'genre']
    