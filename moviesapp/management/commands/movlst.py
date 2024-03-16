from django.core.management.base import BaseCommand
from ...models import Movie


class Command(BaseCommand):
    help = "Shows all movies if there are such"

    def handle(self, *args, **options):
        all_movies = Movie.objects.all()
        # Checks for movies content
        if all_movies:
            # Appends the desire movie info in a list. Representation is title and description, so it will match
            # Django/HTML logic
            movies_list = [
                f"Title: {movie.title} | Description: {movie.description}"
                for movie in all_movies
            ]
            # Adds a text before listing the content
            self.stdout.write("Available movies")
            for movie in movies_list:
                self.stdout.write(movie)
        # If no movies are available let the user know
        else:
            self.stdout.write("No movies are available at this moment")

# TODO next command have to be in separate py file with proper name
