from .models import Movie, Favorites
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import get_object_or_404


# Using annotate (seems like kind of aggregation) to generate query that counts each user who added
# a movie in favorite
def query_sum_favorites_ordered(order: str):
    return Movie.objects.annotate(num_favorites=Count("favorites")).order_by(order)


def query_sum_favorites():
    return Movie.objects.annotate(num_favorites=Count("favorites"))


def query_sum_favorites_filter(some_id: int):
    movies_with_favorites = query_sum_favorites()
    return movies_with_favorites.filter(pk=some_id)


# icontains ensures case-insensitive title search. Constructs complex query that use logical operator OR
def query_complex(query):
    return Movie.objects.filter(Q(title__icontains=query) |
                                Q(director__icontains=query)
                                )


def query_favorite_filter_args(arg_one: int, arg_two: int):
    return Favorites.objects.filter(movie=arg_one, user=arg_two)


def query_get_movie_by_id(some_id: int):
    return get_object_or_404(Movie, pk=some_id)


def add_favorites(user_id: int, movie_id: int):
    return Favorites.objects.create(user=user_id, movie=movie_id)


def query_favorite_filter_one(arg: int):
    return Favorites.objects.filter(user=arg)


def query_get_favorite_by_args(arg_one: int, arg_two: int):
    return get_object_or_404(Favorites, pk=arg_one, user=arg_two)


def query_movie_filter_date_exists(some_date):
    return Movie.objects.filter(release_date=some_date).exists()


def query_movie_filter_title_exists(some_title: str):
    return Movie.objects.filter(title=some_title).exists()


def queryset_movie_form(form):
    return form(queryset=Movie.objects.all(),
                label="Select a movie"
                )

