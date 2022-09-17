from django.shortcuts import render, get_object_or_404
from movie_app.models import Movie
from django.db.models import F, Sum, Min, Max, Count, Avg, Value


# Create your views here.

def show_all_movie(request):
    # movies = Movie.objects.order_by(F('year').asc(nulls_last=True), 'rating')
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
        str_field=Value('hello'),
        int_field=Value(123),
        new_budget=F('budget') + 100,
        new_cadabra=F('rating') + F('year'),
    )
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('id'))
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg,
        'total': movies.count(),
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })


def show_one_director(request, slug_director: str):
    director = get_object_or_404(Movie, slug=slug_director)
    return render(request, 'movie_app/one_movie.html', {
        'director': director
    })