from django.core.management.base import BaseCommand
from ...forms import AddMovieForm
from ...queries_helper import query_insert_movie


class Command(BaseCommand):
    help = "Adding movie to the DB. Required - title,release date ,description, director, gener"

    def add_arguments(self, parser):

        parser.add_argument("title",
                            type=str,
                            help="Title can be maximum 200 characters"
                            )
        parser.add_argument("release_date",
                            type=str,
                            help="Date in format YYYY-MM-DD"
                            )
        parser.add_argument("description",
                            type=str,
                            help="Description can be maximum 230 characters"
                            )
        parser.add_argument("director",
                            type=str,
                            help="Director can be maximum 50 characters"
                            )
        parser.add_argument("gener",
                            type=str,
                            help="""Choose a gener from the first value of the pairs(ex. AN):
                                                                HR - HORROR 
                                                                TR - THRILLER
                                                                RM - ROMANTIC
                                                                AN - ANIMATION
                                                                CM - COMEDY
                                                                FN - FANTASY
                                                                AC - ACTION
                                                                HT - HISTORICAL
                                                                DR - DRAMA
                                                                MT - MYSTERY
                                                                MC - MUSICAL
                                                                CR - CRIME
                                                                AV - ADVENTURE"""
                            )

    def handle(self, *args, **options):
        try:
            # Gets values from the input
            title = options.get("title")
            release_date = options.get("release_date")
            description = options.get("description")
            director = options.get("director")
            gener = options.get("gener")

            # Creating a dictionary with command-line arguments
            data = {
                "title": title,
                "release_date": release_date,
                "description": description,
                "director": director,
                "gener": gener
            }

            # Creating a form instance with the provided data
            form = AddMovieForm(data)
            if form.is_valid():
                # Access validated data through form.cleaned_data
                title = form.cleaned_data["title"]
                release_date = form.cleaned_data["release_date"]
                description = form.cleaned_data["description"]
                director = form.cleaned_data["director"]
                gener = form.cleaned_data["gener"]

                query_insert_movie(title=title,
                                   release_date=release_date,
                                   description=description,
                                   director=director,
                                   gener=gener
                                   )

                self.stdout.write(self.style.SUCCESS(f"Movie saved to the database"))
            else:
                # Unpacks the filed and errors for the form errors
                for field, errors in form.errors.items():
                    for error in errors:
                        self.stderr.write(self.style.ERROR(f"{field}: {error}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
