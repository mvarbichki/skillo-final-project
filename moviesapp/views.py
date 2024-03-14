from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


# the project requirement is that the main page displays movie titles and descriptions
def main_page(request):
    # gets the content from Movie model
    all_movies = Movie.objects.all()
    # presents the movies content as dict for rendering
    movies_context = {
        "all_movies": all_movies,
    }
    return render(request=request,
                  template_name="main_page.html",
                  context=movies_context
                  )


