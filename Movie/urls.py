"""Movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,reverse
from django.shortcuts import redirect

from account import urls
from film import urls
from review import urls
from . import settings
from django.contrib.staticfiles.urls import static
from film.views import MovieListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('movies/', include('film.urls'), name='movies'),
    path('reviews/', include('review.urls')),
    path('', MovieListView.as_view()),
    path('', include('movie-api.urls'))

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)