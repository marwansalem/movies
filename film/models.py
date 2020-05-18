from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    omdb_id = models.CharField(max_length=16, primary_key=True)
    rating = models.DecimalField(max_digits=5, decimal_places=1)
    year = models.SmallIntegerField()
    genre = models.CharField(max_length=32)
    slug = models.SlugField(null=True, blank=True   )
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    def get_absolute_url(self): 
        return reverse('movie_details',kwargs={"title": self.title})