from django.shortcuts import render
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

# TODO work on detail list page
