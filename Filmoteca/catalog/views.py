from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Film, Serie
from .serializers import FilmSerializer, SerieSerializer

# ----- Creamos modelos base genéricos para poder reutilizarlos en los diferentes modelos y asi aplicamos DRY----

class BaseSearchView(generics.ListAPIView):
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class BaseOrderView(generics.ListAPIView):
    filter_backends = [filters.OrderingFilter]
    order_fields = ['title', 'release_date']

# ---- VISTAS DEL MODELO SERIES ----
class SerieListCreate(generics.ListCreateAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer

class SeriesRetriveUpadeteDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer

class SeriesSearch(BaseSearchView):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer

class SerieListOrder(BaseOrderView):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer

# ---- VISTAS DEL MODELO FILMS ----

class FilmsListCreate(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmsRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmSearch(BaseSearchView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class FilmListOrder(BaseOrderView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

# ---- VISTAS APIVIEW  QUE ENLAZA LOS MODELOS----

class CatalogList(APIView):
    def get(self, request):

        films = Film.objects.all()
        series = Serie.objects.all()

        film_serializer = FilmSerializer(films, many=True)
        serie_serializer = SerieSerializer(series, many=True)

        #juntamos los datos de los modelos
        catalog_data = {
            'films': film_serializer.data,
            'series': serie_serializer.data
        }


        return Response(catalog_data)
    

class CatalogSerchByGenre(APIView):

    def get(self, request):

        genre = request.query_params.get('genre', None)

        #comprobamos que el parametro de busqueda no sea nulo
        if genre is None:
            return Response({"error" : "Genre parameter is required"})
        
        films = Film.objects.filter(genre__icontains=genre)
        series = Serie.objects.filter(genre__icontains=genre)

        film_serializer = FilmSerializer(films, many=True)
        serie_serializer = SerieSerializer(series, many=True)

        catalog_data = {
            'films': film_serializer.data,
            'series': serie_serializer.data
        }


        return Response(catalog_data)
    

    
