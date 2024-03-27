from django.core.management.base import BaseCommand
from ...custom_exceptions import UserNotExistException
from ...queries_helper import query_favorite_filter_one, query_user_id_exists


class Command(BaseCommand):
    help = "Shows user favorite movies. Required user ID"

    def add_arguments(self, parser):
        parser.add_argument("user_id", type=int, help="Enter a user ID to to show favorite movies")

    def handle(self, *args, **options):
        user_id = options["user_id"]
        try:
            existing_user = query_user_id_exists(user_id=user_id)

            if not existing_user:
                raise UserNotExistException

            favorites = query_favorite_filter_one(user_id=user_id)
            if favorites:
                for favorite in favorites:
                    self.stdout.write(f"Title: {favorite.movie.title} | Release date: {favorite.movie.release_date}")
            else:
                self.stdout.write("No favorite movies")
        except UserNotExistException:
            self.stdout.write(self.style.ERROR(f"User with ID {user_id} does not exist"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
