from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Film
from .serializers import FilmSerializer

# Create your views here.

class FilmsListCreate(APIView):

    def get(self, request):
        films = Film.objects.all()
        serializer = FilmSerializer(films, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = FilmSerializer(data= request.data)

        #comprobamos que la request sea valida
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
    