from django.core.management.base import BaseCommand
from ...custom_exceptions import UserNotExistException, MovieNotExistException, FavoriteExistException
from ...queries_helper import query_favorite_delete, query_user_id_exists, query_movie_id_exists, \
    query_favorite_filter_args, query_get_user_by_id, query_favorite_filter_one


class Command(BaseCommand):
    help = "Remove user favorite movie. Required user ID and movie ID"

    def add_arguments(self, parser):
        parser.add_argument("user_id", type=int, help="Enter a user ID to which remove the favorite movie")
        parser.add_argument("movie_id", type=int, help="Enter the movie_ID of the desired movie")

    def handle(self, *args, **options):
        user_id = options["user_id"]
        movie_id = options["movie_id"]
        try:
            existing_user = query_user_id_exists(user_id=user_id)
            existing_movie = query_movie_id_exists(movie_id=movie_id)
            existing_favorite_movie = query_favorite_filter_args(movie_id=movie_id, user_id=user_id)

            if not existing_user:
                raise UserNotExistException
            if not existing_movie:
                raise MovieNotExistException
            # If provided movie id that is not in the user's favorite movies it will rise exception
            if not existing_favorite_movie.exists():
                raise FavoriteExistException

            favorites = query_favorite_filter_one(user_id=user_id)
            user = query_get_user_by_id(user_id=user_id)

            for favorite in favorites:
                # From all user's favorite movies finds the correct favorite id by comparing favorite relation movie id
                # with the desire movie id
                if favorite.movie.id == movie_id:
                    query_favorite_delete(favorite_id=favorite.id, user_id=user)

            self.stdout.write(self.style.SUCCESS("The movie removed successfully from your favorites"))

        except FavoriteExistException:
            self.stdout.write(self.style.ERROR("The movie is not in your favorites"))
        except UserNotExistException:
            self.stdout.write(self.style.ERROR(f"User with ID {user_id} does not exist"))
        except MovieNotExistException:
            self.stdout.write(self.style.ERROR(f"Movie with ID {movie_id} does not exist"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
