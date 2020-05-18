from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieListView.as_view()),
    path('<slug>', views.MovieDetailView.as_view(), name='movie_details'),
]
