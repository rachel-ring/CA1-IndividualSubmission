from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Movie
from django.db.models import Q

class MovieListView(ListView):
    model = Movie
    context_object_name = 'movie_list'
    template_name = 'movies/movie_list.html'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    new_comment = None

class MovieCreateView(CreateView):
    model = Movie
    template_name = 'movies/movie_new.html'
    fields = ['title','director', 'description', 'date_released', 'cover']

class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'movies/movie_edit.html'
    fields = ['description']

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = ' movies/movie_delete.html'
    success_url = reverse_lazy('movie_list')

class SearchResultsListView(ListView):
    model = Movie
    context_object_name = 'movie_list'
    template_name = 'movies/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Movie.objects.filter(
            Q(title__icontains=query) | Q(director__icontains=query)
        )