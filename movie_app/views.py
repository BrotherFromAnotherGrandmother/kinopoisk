from django.shortcuts import render, get_object_or_404
from movie_app.models import Movie, Director, Actor
from django.db.models import F, Sum, Min, Max, Count, Avg, Value


# Create your views here.

def show_all_movie(request):
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

def show_all_directors(request):
    directors = Director.objects.all()
    return render(request, 'movie_app/all_directors.html', {
        'directors': directors,
    })

def show_one_dir(request, id_dir: int):
    dir = get_object_or_404(Director, id=id_dir)
    return render(request, 'movie_app/one_dir.html', {
        'dir': dir,
    })

def show_all_actors(request):
    actors = Actor.objects.all()
    return render(request, 'movie_app/all_actors.html', {
        'actors': actors,
    })

def show_one_act(request, id_act: int):
    act = get_object_or_404(Actor, id=id_act)
    return render(request, 'movie_app/one_act.html', {
        'act': act,
    })