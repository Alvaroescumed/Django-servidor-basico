from django.urls import path
from .views import SerieListCreate, SeriesRetriveUpadeteDestroy, FilmsListCreate

urlpatterns = [
    path('series/', SerieListCreate.as_view(), name='actor_list_create'),
    path('series/<int:pk>', SeriesRetriveUpadeteDestroy.as_view(), name='actor_retrive_update_destroy'),
    path('films/', FilmsListCreate.as_view(), name='films_list_create')
]