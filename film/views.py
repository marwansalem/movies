from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie
# Create your views here.

class MovieListView(ListView):
    paginate_by = 10
    context_object_name='movies_cont'
    template_tag = 'all_movies.html'
    model = Movie
    ordering = ['title']

class MovieDetailView(DetailView):
    model = Movie