from rest_framework import serializers
from film.models import Movie

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'rating')
        