from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm
from .models import Account
from review.models import UserReview
from django.views.generic import ListView, DetailView
# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('/movies')
    if request.method == 'POST':
        userform = UserForm(request.POST)
        profileform = ProfileForm(request.POST)
        if userform.is_valid() and profileform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()

            profile = profileform.save(commit=False)
            profile.user = user
            if 'profile_picture' in request.FILES:
                profile.pic = request.FILES['profile_picture']
            profile.save()
            return redirect('/movies')
        else:
            print("Error",userform.errors," Profile forms",profileform.errors)
    else:
        userform = UserForm()
        profileform = ProfileForm()
    return render(request,'register.html', {'userform':userform,
    'profileform':profileform})

class UserDetailView(DetailView):
    model = Account

class UserReviewsListView(ListView):
    paginate_by = 10
    context_object_name='review_context'
    template_tag = 'review_list.html'
    model = UserReview
    ordering = ['user_rating']
    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['accs'] = Account
       
        return context