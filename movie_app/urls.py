from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors/<slug:slug_movie>', views.show_one_director, name='director-detail'),
]
