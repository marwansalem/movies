from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie
from review.models import UserReview
# Create your views here.

class MovieListView(ListView):
    paginate_by = 10
    context_object_name='movies_cont'
    template_tag = 'all_movies.html'
    model = Movie
    ordering = ['title']

class MovieDetailView(DetailView):
    #context_object_name='movie_details'
    model = Movie

class MovieReviewsListView(ListView):
    paginate_by = 10
    ordering = ['user_rating']
    template_tag = 'movie_user_review.html'
    model = UserReview