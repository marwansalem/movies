from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import UserReviewCreateView, UserReviewDetailView, UserReviewDeleteView

urlpatterns = [
     path('create/<omdb_id>', login_required(UserReviewCreateView.as_view(),login_url='login'), name="create_review"),
     path('<slug>/', login_required(UserReviewDetailView.as_view(),login_url='login'), name='review_details'),
     path('<slug>/delete/', login_required(UserReviewDeleteView.as_view() ,login_url='login'), name='delete_review')
]
