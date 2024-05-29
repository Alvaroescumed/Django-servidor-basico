
from rest_framework import generics
from .models import Film, Serie
from .serializers import FilmSerializer, SerieSerializer

class SerieListCreate(generics.ListCreateAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer

class SeriesRetriveUpadeteDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer

class FilmsListCreate(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmsRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    