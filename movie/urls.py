from django.urls import path
from .views import MovieListView, MovieDetailView, SearchResultsListView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('<uuid:pk>', MovieDetailView.as_view(), name='movie_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]
