from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Favorites
from .forms import AddMovieForm, RegisterForm, LoginForm, FavoritesMovieForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .custom_exceptions import FavoriteExistException
from django.db.models import Count


# The main page of the web app. It contains all the paths to site functionalities
def main_page(request):
    return render(request=request,
                  template_name="main_page.html"
                  )


def available_movies_page(request):
    # Gets the sorting category from the HTML request depending on order_by's value
    order_by = request.GET.get("order")
    # Using annotate (seems like kind of aggregation) to generate query that counts each user who added
    # a movie in favorite
    if order_by == "likes":
        # Release date is presented in descending favorites
        sorted_movies = Movie.objects.annotate(num_favorites=Count("favorites")).order_by("-num_favorites")
    elif order_by == "release_date":
        # Release date is presented in descending order
        sorted_movies = Movie.objects.annotate(num_favorites=Count("favorites")).order_by("-release_date")
    elif order_by == "gener":
        sorted_movies = Movie.objects.annotate(num_favorites=Count("favorites")).order_by("gener")
    else:
        # Gets default order
        sorted_movies = Movie.objects.annotate(num_favorites=Count("favorites"))
    # Presents the movies as dict context for the rendering
    return render(request=request,
                  template_name="available_movies_page.html",
                  context={"sorted_movies": sorted_movies}
                  )


# Details view for given movie that display the whole info about it in separate html page
def details_page(request, movie_id):
    # Gets the aggregated query with the counted favorite for all movies
    movies_with_favorites = Movie.objects.annotate(num_favorites=Count("favorites"))
    # Gets the result for the given movie by an id
    movie_elements = movies_with_favorites.filter(pk=movie_id)
    return render(request=request,
                  context={"movie_elements": movie_elements},
                  template_name="details_page.html"
                  )


# The view for the search movie logic
def search_page(request):
    # Gets the searched value from the HTML input "name=q"
    query = request.GET.get("q")
    # icontains ensures case-insensitive title search
    results = Movie.objects.filter(title__icontains=query)
    return render(request=request,
                  template_name="result_page.html",
                  context={"results": results}
                  )


# Add movie logic
def add_movie_page(request):
    # If form is not valid it will return the raised exception as message taken from validation form(AddMovieForm) to
    # the user. For example, I'm handling the release date to be in a certain range
    form = AddMovieForm()
    if request.POST:
        form = AddMovieForm(request.POST, request.FILES)
        # If input data is valid, then save the movie in the DB
        if form.is_valid():
            form.save()
            return redirect(main_page)
    return render(request=request,
                  template_name="add_movie_page.html",
                  context={"form": form}
                  )


@login_required(login_url="user_login")
def add_favorites_page(request):
    form = FavoritesMovieForm()
    try:
        if request.method == "POST":
            form = FavoritesMovieForm(request.POST)
            if form.is_valid():
                # Gets the movie id which is passed from the form
                movie_id = form.cleaned_data["movie"].id
                # Gets if there is a match by movie id and user id in Favorite model
                existing_favorite_movie = Favorites.objects.filter(movie=movie_id, user=request.user)
                # If it doesn't return any result it means the movie is not in the user's favorite yet
                if not existing_favorite_movie:
                    movie = get_object_or_404(Movie, pk=movie_id)
                    # Establishing the relation between a user and a movie in the Favorites model
                    Favorites.objects.create(user=request.user, movie=movie)
                    return redirect(show_favorites_page)
                else:
                    # If the movie is already in the user's favorite it will raise an exception
                    raise FavoriteExistException("The movie is already in your favorites")
    except FavoriteExistException as e:
        # Passing the exception message to the base template
        request.error_message = str(e)
    return render(request=request,
                  template_name="add_favorites_page.html",
                  context={"form": form}
                  )


# Decorator that allows only logged-in users to reach the function. If the user is not logged in its redirect
# to the login page
@login_required(login_url="user_login")
def show_favorites_page(request):
    # Returns pair user-movies from Favorites based the logged user
    favorites = Favorites.objects.filter(user=request.user)
    return render(request=request,
                  template_name="show_favorites_page.html",
                  context={"favorites": favorites}
                  )


@login_required(login_url="user_login")
def remove_favorites_page(request, favorite_id):
    if request.method == "POST":
        favorite = get_object_or_404(Favorites, pk=favorite_id, user=request.user)
        favorite.delete()
        return redirect(show_favorites_page)


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(user_login)
    return render(request=request,
                  template_name="register.html",
                  context={"form": form}
                  )


def user_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            # Authenticate the input information by comparing to the User model
            user = authenticate(request, username=username, password=password)
            # If authentication is successful allow the user to log in
            if user is not None:
                auth.login(request, user)
                return redirect(main_page)
    return render(request=request,
                  template_name="login.html",
                  context={"form": form}
                  )


@login_required(login_url="user_login")
def user_logout(request):
    auth.logout(request)
    return redirect(main_page)

# TODO add exceptions and final retest
