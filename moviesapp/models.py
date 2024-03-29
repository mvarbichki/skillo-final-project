from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    # Subclass enumeration types to define choices. Will be used in the front end as drop-down menu of choices
    class Genres(models.TextChoices):
        # The first value is stored in the DB and the second values is human-readable show in the drop-down
        HORROR = "HR", "HORROR"
        THRILLER = "TR", "THRILLER"
        ROMANTIC = "RM", "ROMANTIC"
        ANIMATION = "AN", "ANIMATION"
        COMEDY = "CM", "COMEDY"
        FANTASY = "FN", "FANTASY"
        ACTION = "AC", "ACTION"
        HISTORICAL = "HT", "HISTORICAL"
        DRAMA = "DR", "DRAMA"
        MYSTERY = "MT", "MYSTERY"
        MUSICAL = "MC", "MUSICAL"
        CRIME = "CR", "CRIME"
        ADVENTURE = "AV", "ADVENTURE"

    # After a brief check in the internet decided to give 200 characters for the title because the longest movie name
    # has around 200c
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=230)
    release_date = models.DateField()
    # I did same check for director name, as longest know human name is around 50c
    director = models.CharField(max_length=53)
    # For gener I'll implement the build in Django option for drop down choices
    gener = models.CharField(max_length=20,
                             choices=Genres.choices
                             )
    # Upload cover img for each movie. Allows this field to be empty
    cover = models.ImageField(upload_to="moviesapp/covers",
                              blank=True
                              )

    def __str__(self):
        return f"{self.title}, {self.description}, {self.release_date}, {self.director}, {self.gener}"

    # Manipulating the string fields of the model. Before write them in the DB all str data will be converted to
    # upper(). At this point I would like to avoid dealing with words that should be first-letter capital
    def save(self, *args, **kwargs):
        if isinstance(self.title, str):
            self.title = self.title.upper()
        if isinstance(self.description, str):
            self.description = self.description.upper()
        if isinstance(self.director, str):
            self.director = self.director.upper()

        super().save(*args, **kwargs)


# Favorites model will carry the favorites movies logic. It creates relations fk to users in the build-in User model
# and one to the Movie model. Via these relations the Favorites keeps all favorite movies for each user.
# If a given Movie or User model record is deleted the relation will be deleted from Favorites as well
class Favorites(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE
                             )
    movie = models.ForeignKey(Movie,
                              on_delete=models.CASCADE
                              )

    def __str__(self):
        return f"{self.movie}, {self.user}"
