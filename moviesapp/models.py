from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
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

    # After a brief check in the internet decided to give 200 characters for the title because the longest movie name
    # has around 200c
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=230)
    # I'll store the release year as example - 1998, so will use SmallPositiveInt
    release_year = models.PositiveSmallIntegerField()
    # I did same check for director name, as longest know human name is around 50c
    director = models.CharField(max_length=53)
    # For gener I'll implement the build in Django option for drop down choices
    gener = models.CharField(max_length=20, choices=Genres.choices)
    # I'll make relation between build-in User model and my own model via Many-to-Many relation. This way I'll store
    # each user like for a given movie. Allows this field to be empty
    users_likes = models.ManyToManyField(User, blank=True)
    # Upload cover img for each movie in moviesapp/covers. Allows this field to be empty
    cover = models.ImageField(upload_to="moviesapp/covers", blank=True)
