from .models import Movie, Favorites
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


# Using annotate (seems like kind of aggregation) to generate query that counts each user who added
# a movie in favorite
def query_sum_favorites_ordered(order: str):
    return Movie.objects.annotate(num_favorites=Count("favorites")).order_by(order)


def query_sum_favorites():
    return Movie.objects.annotate(num_favorites=Count("favorites"))


def query_sum_favorites_filter(movie_id: int):
    movies_with_favorites = query_sum_favorites()
    return movies_with_favorites.filter(pk=movie_id)


# icontains ensures case-insensitive title search. Constructs complex query that use logical operator OR
def query_complex(query):
    return Movie.objects.filter(Q(title__icontains=query) |
                                Q(director__icontains=query)
                                )


def query_favorite_filter_args(movie_id: int, user_id: int):
    return Favorites.objects.filter(movie=movie_id, user=user_id)


def query_get_movie_by_id(movie_id: int):
    return get_object_or_404(Movie, pk=movie_id)


def query_get_user_by_id(user_id: int):
    return get_object_or_404(User, pk=user_id)


def query_insert_favorites(user_id: int, movie_id: int):
    return Favorites.objects.create(user=user_id, movie=movie_id)


def query_favorite_filter_one(user_id: int):
    return Favorites.objects.filter(user=user_id)


def query_get_favorite_by_args(favorite_id: int, user_id: int):
    return get_object_or_404(Favorites, pk=favorite_id, user=user_id)


def query_movie_filter_date_exists(some_date):
    return Movie.objects.filter(release_date=some_date).exists()


def query_movie_filter_title_exists(some_title: str):
    return Movie.objects.filter(title=some_title).exists()


def queryset_movie_form(form):
    return form(queryset=Movie.objects.all(),
                label="Select a movie"
                )


def query_user_id_exists(user_id):
    return User.objects.filter(id=user_id).exists()


def query_movie_id_exists(movie_id):
    return Movie.objects.filter(id=movie_id).exists()


def queries_order_picker(order_by):
    if order_by == "likes":
        # Release date is presented in descending favorites. Shows only the first 5 results
        return query_sum_favorites_ordered("-num_favorites")[:5]
    elif order_by == "release_date":
        # Release date is presented in descending order. Shows only the first 5 results
        return query_sum_favorites_ordered("-release_date")[:5]
    elif order_by == "gener":
        # Returns by alphabetical order of genres
        return query_sum_favorites_ordered("gener")
    else:
        # Default order
        return query_sum_favorites()


def query_insert_movie(title: str, release_date: str, description: str, director: str, gener: str):
    new_movie = Movie(title=title,
                      release_date=release_date,
                      description=description,
                      director=director,
                      gener=gener
                      )
    new_movie.save()


def query_favorite_delete(favorite_id: int, user_id: int):
    favorite = query_get_favorite_by_args(favorite_id, user_id)
    favorite.delete()
