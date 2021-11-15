from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Movie
# from .forms import CommentForm
# from django.shortcuts import render, get_object_or_404
from django.db.models import Q

class MovieListView(ListView):
    model = Movie
    context_object_name = 'movie_list'
    template_name = 'movies/movie_list.html'
class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    new_comment = None


class SearchResultsListView(ListView):
    model = Movie
    context_object_name = 'movie_list'
    template_name = 'movies/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Movie.objects.filter(
            Q(title__icontains=query) | Q(director__icontains=query)
        )