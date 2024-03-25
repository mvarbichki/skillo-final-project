from django.core.management.base import BaseCommand
from ...custom_exceptions import FavoriteExistException, MovieNotExistException, UserNotExistException
from ...queries_helper import query_insert_favorites, query_get_movie_by_id, query_favorite_filter_args, \
                               query_user_id_exists, query_movie_id_exists, query_get_user_by_id


class Command(BaseCommand):
    help = "Adding a movie to favorite. Required user ID and movie ID"

    def add_arguments(self, parser):
        parser.add_argument("user_id", type=int, help="Provide a user ID to which adding the favorite movie")
        parser.add_argument("movie_id", type=int, help="Provide the movie_ID of the desired movie")

    def handle(self, *args, **options):
        movie_id = options["movie_id"]
        user_id = options["user_id"]

        try:
            existing_user = query_user_id_exists(user_id=user_id)
            existing_movie = query_movie_id_exists(movie_id=movie_id)
            existing_favorite_movie = query_favorite_filter_args(movie_id=movie_id, user_id=user_id)

            if not existing_user:
                raise UserNotExistException
            if not existing_movie:
                raise MovieNotExistException
            if existing_favorite_movie.exists():
                raise FavoriteExistException

            movie = query_get_movie_by_id(movie_id=movie_id)
            user = query_get_user_by_id(user_id=user_id)
            query_insert_favorites(user_id=user, movie_id=movie)
            self.stdout.write(self.style.SUCCESS("The movie added successfully to your favorites"))

        except FavoriteExistException:
            self.stdout.write(self.style.ERROR("The movie is already in your favorites"))
        except UserNotExistException:
            self.stdout.write(self.style.ERROR("The user not exist"))
        except MovieNotExistException:
            self.stdout.write(self.style.ERROR("The movie not exist"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
