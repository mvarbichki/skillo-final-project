from django.core.management.base import BaseCommand
from ...custom_exceptions import MovieNotExistException
from ...queries_helper import query_movie_id_exists, query_movie_delete


class Command(BaseCommand):
    help = "Remove a movie. Required movie ID"

    def add_arguments(self, parser):
        parser.add_argument("movie_id",
                            type=int,
                            help="Enter the id of the movie you want to delete"
                            )

    def handle(self, *args, **options):
        movie_id = options["movie_id"]
        try:
            existing_movie = query_movie_id_exists(movie_id=movie_id)

            if not existing_movie:
                raise MovieNotExistException

            query_movie_delete(movie_id=movie_id)

            self.stdout.write(self.style.SUCCESS("The movie removed successfully"))

        except MovieNotExistException:
            self.stdout.write(self.style.ERROR(f"Movie with ID {movie_id} does not exist"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
