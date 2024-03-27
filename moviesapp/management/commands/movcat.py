from django.core.management.base import BaseCommand
from ...queries_helper import queries_order_picker


class Command(BaseCommand):
    help = "Returns movies ordered by desired categories"

    def add_arguments(self, parser):
        # Adds argument as required limited option from a list
        parser.add_argument(
            "--option",
            choices=["default", "gener", "likes", "release_date"],
            help="Choose one of the available options (default, gener, likes, release_date)."
                 " Example:  movcat --option gener",
            required=True
        )

    def handle(self, *args, **options):
        try:
            category = options['option']
            sorted_movies = queries_order_picker(order_by=category)
            self.stdout.write(f"Movies result by {category}")
            for movie in sorted_movies:
                self.stdout.write(f"Title: {movie.title} {movie.release_date} | Gener: {movie.get_gener_display()} | "
                                  f"Description: {movie.description} |  Users rating: {movie.num_favorites}")
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
