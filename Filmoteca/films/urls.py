from django.urls import path
from .views import FilmsListCreate

urlpatterns = [
    path('films/', FilmsListCreate.as_view(), name='film_list_create')
]