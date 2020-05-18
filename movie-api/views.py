from rest_framework import viewsets

from django.db.models import F
from .serializers import MovieSerializer
from film.models import Movie


class MovieViewSet(viewsets.ModelViewSet):
    #get top 10 movies
    queryset = Movie.objects.all().order_by('-rating')[0:10]
    print(len(queryset))
    
    serializer_class = MovieSerializer