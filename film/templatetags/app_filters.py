from django import template
from Movie.settings import OMDB_API_KEY
register = template.Library()


# filter that take the omdb_id from the movie object and through filter
#converts it into the api request
@register.filter
def poster_url(movie_id):
    return f'http://img.omdbapi.com/?apikey={OMDB_API_KEY}&i={movie_id}'
