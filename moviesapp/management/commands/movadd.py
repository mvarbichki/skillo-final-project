from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Adding movie to the DB. Required - title,release date ,description, director, gener"

    def add_arguments(self, parser):
        parser.add_argument("title", type=str, help="Title can be maximum 200 characters")
        parser.add_argument("release_date", type=str, help="Date in format YYYY-MM-DD")
        parser.add_argument("description", type=str, help="Description can be maximum 230 characters")
        parser.add_argument("director", type=str, help="Director can be maximum 50 characters")
        parser.add_argument("gener", type=str, help="Gener can be maximum 20 characters")

    def handle(self, *args, **options):
        pass
