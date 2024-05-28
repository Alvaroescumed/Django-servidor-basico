from rest_framework import serializers
from .models import Film, Actor

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor,
        fields = ['id', 'name', 'birth_date']

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'actors', 'release_date', 'genre']
    