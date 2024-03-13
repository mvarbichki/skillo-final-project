from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


# the project requirement is that the main page displays movie titles and descriptions
def main_page(request):
    movies_list = []
    all_movies = Movie.objects.all()
    # TODO display title and description of all movies in the main page html IF model is empty display - no content
    l = [movies_list.append(f"Title: {movie.title} - description: {movie.description}") for movie in all_movies]
    return render(request=request,
                  template_name="main_page.html"
                  )
