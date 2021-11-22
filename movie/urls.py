from django.urls import path
from .views import(
    MovieListView, 
    MovieDetailView,
    MovieUpdateView,
    SearchResultsListView,
    MovieCreateView,
    MovieDeleteView
    ) 

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('movie/<uuid:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('movie/new/', MovieCreateView.as_view(), name='movie_new'),
    path('<uuid:pk>/edit/', MovieUpdateView.as_view(), name='movie_edit'),
    path('<uuid:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),
]
