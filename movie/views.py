from django.views.generic import ListView, DetailView
from .models import Movie

class MovieListView(ListView):
    model = Movie
    context_object_name = 'movie_list'
    template_name = 'movies/movie_list.html'
class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'