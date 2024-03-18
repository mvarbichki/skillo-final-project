from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import AddMovieForm


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
    # Gets it as object by id and renders it. If not existing id is given it will pop - http 404
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request=request,
                  context={"movie": movie},
                  template_name="details_page.html"
                  )


# Search view for the search movies logic
def search_page(request):
    # Gets the searched value from the HTML input name=q
    query = request.GET.get("q")
    # icontains ensures case-insensitive title search
    results = Movie.objects.filter(title__icontains=query)
    return render(request=request,
                  template_name="result_page.html",
                  context={"results": results}
                  )


# Add movie logic
def add_movie_page(request):
    if request.POST:
        form = AddMovieForm(request.POST, request.FILES)
        # if form validation is passed it will record the data in teh DB
        if form.is_valid():
            form.save()
            return redirect(listing_page)
    return render(request=request,
                  template_name="add_movie_page.html",
                  context={"form": AddMovieForm}
                  )

# TODO find a way to rise messages or redirect to page with message
