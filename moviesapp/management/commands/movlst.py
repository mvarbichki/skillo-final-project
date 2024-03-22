from django.core.management.base import BaseCommand
from ...queries_helper import query_sum_favorites


class Command(BaseCommand):
    help = "Displaying movies if there any"

    def handle(self, *args, **options):
        all_movies = query_sum_favorites()
        # Checks for movies content
        if all_movies:
            movies_list = (
                f"Title: {movie.title} - {movie.release_date} | Description: {movie.description}"
                for movie in all_movies
            )
            self.stdout.write("Available movies")
            for movie in movies_list:
                self.stdout.write(movie)
        else:
            self.stdout.write("No movies are available at this moment")
