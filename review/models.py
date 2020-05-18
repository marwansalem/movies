from django.db import models
from film.models import Movie
from account.models import Account
# Create your models here.

class UserReview(models.Model):
    #
    #movie = models.ManyToManyField(Movie, related_name='review_movie')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE , related_name='review_movie')
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user_review',)
    review_body = models.CharField(max_length=500)
    user_rating = models.CharField(max_length=1, choices=(('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5')) )
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.self.movie.omdb_id +':' + self.author + self.user_rating