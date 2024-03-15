from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Shows all movies"

    def handle(self, *args, **options):
        self.stdout.write("CLI TEST")
