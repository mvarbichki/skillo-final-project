from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Movie


# The project requirement is that the main page displays movie titles and descriptions
def listing_page(request):
    # Gets the content from Movie model
    all_movies = Movie.objects.all()
    # Presents the movies content as dict context for the rendering
    return render(request=request,
                  template_name="listing_page.html",
                  context={"all_movies": all_movies}
                  )


# Details view for given movie that display the whole info about it in separate html page
def details_page(request, movie_id):
    # Gets it as object by id and render it. If not existing id is given it will pop - http 404
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request=request,
                  context={"movie": movie},
                  template_name="details_page.html"
                  )

# TODO figure out how django users works. Find a way to show the number of users likes if there are such for a given movie
