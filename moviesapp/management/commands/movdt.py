from django.core.management.base import BaseCommand
from ...custom_exceptions import MovieNotExistException
from ...queries_helper import query_sum_favorites_filter


class Command(BaseCommand):
    help = "Displaying movie details if the movie exists in the DB. Movie id required"

    # Instructs the command to expect an argument. In this case is movie_id
    def add_arguments(self, parser):
        parser.add_argument("movie_id", type=int)

    def handle(self, *args, **options):
        movie_id = options["movie_id"]
        try:
            movie_elements = query_sum_favorites_filter(movie_id)

            # Raise exception if the movie not exist
            if not movie_elements.exists():
                raise MovieNotExistException

            self.stdout.write("Movie details")
            for element in movie_elements:
                self.stdout.write(f"Title: {element.title}")
                self.stdout.write(f"Release year: {element.release_date}")
                self.stdout.write(f"Description: {element.description}")
                self.stdout.write(f"Director: {element.director}")
                self.stdout.write(f"Gener: {element.get_gener_display()}")
                self.stdout.write(f"User ratings: {element.num_favorites }")

        except MovieNotExistException:
            self.stdout.write(self.style.ERROR(f"Movie with ID {movie_id} does not exist"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
