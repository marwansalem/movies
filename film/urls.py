from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', views.MovieListView.as_view()),
    path('<slug>/', views.MovieDetailView.as_view(), name='movie_details'),
]
