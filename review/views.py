from django.shortcuts import render
from django.views.generic import CreateView,DetailView,DeleteView
from .models import UserReview
from film.models import Movie
from account.models import Account
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
# Create your views here.

class UserReviewCreateView(CreateView):
    fields = ('review_body','user_rating')
    model = UserReview
    def form_valid(self, form):
        movie = Movie.objects.get(pk=self.kwargs['omdb_id'])
        user = self.request.user
        acc = Account.objects.get(user=user)
        
        if len(UserReview.objects.filter(author=acc,movie=movie))!=0:
            return HttpResponseRedirect('/movies')
        
        
        form.instance.author = acc 
        form.instance.movie = movie
        return super(UserReviewCreateView, self).form_valid(form)

class UserReviewDetailView(DetailView):
    #fields = ('review_body','user_rating')
    model = UserReview
    
class UserReviewDeleteView(DeleteView):
    model = UserReview
    # bcuz after deleting u cant return to the deleted category page
    success_url = reverse_lazy('movies')


    