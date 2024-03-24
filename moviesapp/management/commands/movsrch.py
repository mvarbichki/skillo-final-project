from django.core.management.base import BaseCommand
from ...queries_helper import query_complex


class Command(BaseCommand):
    help = "Search a movie by title or director. User input required after execute the command"

    def handle(self, *args, **options):
        search_input = input("Search a movie (by title or director): ")
        results = query_complex(search_input)
        if results:
            self.stdout.write(self.style.SUCCESS(f"Search results"))
            for result in results:
                self.stdout.write(self.style.SUCCESS(f"Title: {result.title} {result.release_date}"
                                                     f" | Director: {result.director}"))
        else:
            self.stdout.write(self.style.SUCCESS("No results found"))
