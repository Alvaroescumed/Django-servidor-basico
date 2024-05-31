from django.urls import path
from .views import SerieListCreate, SeriesRetriveUpadeteDestroy, FilmsListCreate, FilmsRetriveUpdateDestroy, CatalogList, CatalogSerchByGenre, SeriesSearch, FilmSearch, SerieListOrder, FilmListOrder

urlpatterns = [
    path('series/', SerieListCreate.as_view(), name='serie_list_create'),
    path('series/<int:pk>', SeriesRetriveUpadeteDestroy.as_view(), name='serie_retrive_update_destroy'),
    path('series/search/', SeriesSearch.as_view(), name='serie_search'),
    path('series/order/', SerieListOrder.as_view(), name='serie_list_order'),
    path('films/', FilmsListCreate.as_view(), name='films_list_create'),
    path('films/<int:pk>', FilmsRetriveUpdateDestroy.as_view(), name='film__retrive_update_destroy'),
    path('films/search/', FilmSearch.as_view(), name='film_search'),
    path('films/order/', FilmListOrder.as_view(), name='film_list_order'),
    path('catalog/', CatalogList.as_view(), name='catalog_list'),
    path('catalog/search/', CatalogSerchByGenre.as_view(), name='catalog_search_by_genre')
]
