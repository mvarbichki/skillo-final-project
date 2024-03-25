from django.core.management.base import BaseCommand
from ...queries_helper import query_complex
from ...utilities import input_required


class Command(BaseCommand):
    help = ("Search a movie by title or director. Here the approach is different and no argument is needed."
            "User input is required after executing the command")

    def handle(self, *args, **options):
        try:
            search_input = input("Search a movie (by title or director): ")
            # Since search logic is required in the Django/HTML, the CLI search logic input required as well
            required_input = input_required(search_input=search_input,
                                            input_massage="Input required! Type 'q' to exit or type title/director: "
                                            )
            results = query_complex(required_input)
            if results:
                self.stdout.write(self.style.SUCCESS("Search results"))
                for result in results:
                    self.stdout.write(self.style.SUCCESS(f"Title: {result.title} {result.release_date}"
                                                         f" | Director: {result.director}"))
            else:
                self.stdout.write(self.style.SUCCESS("No results found"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
