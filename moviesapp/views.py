from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Favorites
from .forms import AddMovieForm, RegisterForm, LoginForm, FavoritesMovieForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


# The project requirement says the main page has to display movie titles and descriptions
def listing_page(request):
    # Gets the content from Movie model
    all_movies = Movie.objects.all()
    # Presents the movies as dict context for the rendering
    return render(request=request,
                  template_name="listing_page.html",
                  context={"all_movies": all_movies}
                  )


# Details view for given movie that display the whole info about it in separate html page
def details_page(request, movie_id):
    # Gets the movie by id and renders it. If not existing id is given it will pop - http 404
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request=request,
                  context={"movie": movie},
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
            return redirect(listing_page)
    return render(request=request,
                  template_name="add_movie_page.html",
                  context={"form": form}
                  )


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
                return redirect(listing_page)
    return render(request=request,
                  template_name="login.html",
                  context={"form": form}
                  )


def user_logout(request):
    auth.logout(request)
    return redirect(listing_page)


@login_required(login_url="user_login")
def add_favorites_page(request):
    # TODO find a way to display only movies that are not in favorites yet
    form = FavoritesMovieForm()
    if request.method == "POST":
        form = FavoritesMovieForm(request.POST)
        if form.is_valid():
            # Gets the movie id which is passed from the form
            movie_id = form.cleaned_data["movie"].id
            movie = get_object_or_404(Movie, pk=movie_id)
            # Establishing the relation between a user and a movie in the Favorites model
            Favorites.objects.create(user=request.user, movie=movie)
            return redirect(show_favorites_page)
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
