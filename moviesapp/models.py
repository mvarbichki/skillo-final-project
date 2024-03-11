from django.db import models


class Movies(models.Model):
    # Subclass enumeration types to define choices. Will be used in the front end as drop-down menu of choices
    class Genres(models.TextChoices):
        # The first value is stored in the DB and the second values is human-readable show in the drop-down
        HORROR = "HR", "Horror"
        THRILLER = "TR", "Thriller"
        ROMANTIC = "RM", "Romantic"
        ANIMATION = "AN", "Animation"
        COMEDY = "CM", "Comedy"
        FANTASY = "FN", "Fantasy"
        ACTION = "AC", "Action/Adventure"
        HISTORICAL = "HT", "Historical"
        DRAMA = "DR", "Drama"
        MYSTERY = "MT", "Mystery"
        MUSICAL = "MC", "Musical"
        CRIME = "CR", "Crime"

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=230)
    release_year = models.PositiveSmallIntegerField()
    director = models.CharField(max_length=53)
    gener = models.CharField(max_length=20, choices=Genres.choices)
    # TODO how to store the user_likes?
    users_likes = ""
