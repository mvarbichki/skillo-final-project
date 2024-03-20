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
    release_date = models.DateField()
    # I did same check for director name, as longest know human name is around 50c
    director = models.CharField(max_length=53)
    # For gener I'll implement the build in Django option for drop down choices
    gener = models.CharField(max_length=20, choices=Genres.choices)
    # Upload cover img for each movie in moviesapp/covers. Allows this field to be empty
    cover = models.ImageField(upload_to="moviesapp/covers", blank=True)

    def __str__(self):
        return f"{self.title}, {self.description}, {self.release_date}, {self.director}, {self.gener}"


# Favorites model will carry the favorites movies logic. It creates relations fk. On to users in the build-in User model
# and one to Movie model. Via these relations the model keeps all favorites movies for each user.
# If a given Movie or User model record is deleted the relation will be deleted from Favorites as well
class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
