from django.db import models
from film.models import Movie
from account.models import Account
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.

class UserReview(models.Model):
    #
    #movie = models.ManyToManyField(Movie, related_name='review_movie')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE , related_name='review_movie')
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user_review',)
    review_body = models.TextField(max_length=500)
    user_rating = models.CharField(max_length=1, choices=(('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5')) )
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(primary_key=True )
    def get_absolute_url(self):#cbv 37 
        return reverse('review_details', kwargs={"slug": self.slug})
    def __str__(self):
        return self.movie.omdb_id +'-' + self.author.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.__str__())
        super(UserReview, self).save(*args, **kwargs)