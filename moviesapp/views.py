from django.shortcuts import render, redirect
from .forms import AddMovieForm, RegisterForm, LoginForm, FavoritesMovieForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .custom_exceptions import FavoriteExistException
from .queries_helper import query_sum_favorites_filter, query_complex, query_favorite_filter_args, query_favorite_delete, \
    query_get_movie_by_id, query_insert_favorites, query_favorite_filter_one, queries_order_picker


# The main page of the web app. It contains all the paths to site functionalities
def main_page(request):
    return render(request=request,
                  template_name="main_page.html"
                  )


def available_movies_page(request):
    # Gets the sorting category from the HTML request depending on order value
    category = request.GET.get("order")
    sorted_movies = queries_order_picker(order_by=category)
    return render(request=request,
                  template_name="available_movies_page.html",
                  context={"sorted_movies": sorted_movies}
                  )


# Details view for given movie that display the whole info about it in separate html page
def details_page(request, movie_id):
    # Gets the result for the given movie by an id
    movie_elements = query_sum_favorites_filter(movie_id)
    return render(request=request,
                  context={"movie_elements": movie_elements},
                  template_name="details_page.html"
                  )


# The view for the search movie logic
def search_page(request):
    # Gets the searched value from the HTML input "name=q"
    query = request.GET.get("q")
    results = query_complex(query)
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
            return redirect(available_movies_page)
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
                # Gets result if there is a match by movie id and user id in Favorite model
                existing_favorite_movie = query_favorite_filter_args(movie_id, request.user)
                # If it doesn't return any result it means the movie is not in the user's favorite yet
                if not existing_favorite_movie:
                    movie = query_get_movie_by_id(movie_id)
                    # Establishing the relation between a user and a movie in the Favorites model
                    query_insert_favorites(request.user, movie)
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
    favorites = query_favorite_filter_one(request.user)
    return render(request=request,
                  template_name="show_favorites_page.html",
                  context={"favorites": favorites}
                  )


@login_required(login_url="user_login")
def remove_favorites_page(request, favorite_id):
    if request.method == "POST":
        query_favorite_delete(favorite_id=favorite_id, user_id=request.user)
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
