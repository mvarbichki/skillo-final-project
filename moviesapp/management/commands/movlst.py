from django.core.management.base import BaseCommand
from ...queries_helper import query_sum_favorites


class Command(BaseCommand):
    help = "Displaying movies if there any"

    def handle(self, *args, **options):
        try:
            all_movies = query_sum_favorites()
            # Checks for movies content
            if all_movies:
                # Gets only the desired information from result in a tuple
                movies_list = (
                    f"Title: {movie.title} - {movie.release_date} | Description: {movie.description}"
                    for movie in all_movies
                )
                self.stdout.write("Available movies")
                for movie in movies_list:
                    self.stdout.write(movie)
            else:
                self.stdout.write("No movies are available at this moment")
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))