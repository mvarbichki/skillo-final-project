from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Movie


# the project requirement is that the main page displays movie titles and descriptions
def listing_page(request):
    # gets the content from Movie model
    all_movies = Movie.objects.all()
    # presents the movies content as dict context for the rendering
    return render(request=request,
                  template_name="listing_page.html",
                  context={"all_movies": all_movies}
                  )


# details view for given movie that display the whole info about it in separate html page
def details_page(request, movie_id):
    # gets it as object by id and render it. If not existing id is given it will pop - Page not found (404)
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request=request,
                  context={"movie": movie},
                  template_name="details_page.html"
                  )

# TODO find a way to show the cover pic if exist and the number of users likes if there are such
