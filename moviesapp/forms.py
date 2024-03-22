from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError
from .models import Movie
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from .queries_helper import query_movie_filter_date_exists, query_movie_filter_title_exists, queryset_movie_form


# Validation form for adding movie
class AddMovieForm(forms.ModelForm):
    # Adds label to each field and sets required
    title = forms.CharField(
        label="Title: *",
        required=True
    )
    description = forms.CharField(
        label="Description *",
        required=True
    )
    director = forms.CharField(
        label="Director *",
        required=True
    )
    release_date = forms.DateField(
        label="Release date *",
        required=True,
        # Adds calendar widget
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
    )
    cover = forms.ImageField(
        label="Cover image",
        required=False
    )

    def clean_release_date(self):
        # access the form input title and release_date
        form_date = self.cleaned_data["release_date"]
        from_title = self.cleaned_data["title"]
        # All date values are in date() format so they can be compared to each other
        # Restricting user input minimum date be 1895-12-28 (the first official release date of a movie)
        min_date = datetime(1895, 12, 28).date()
        # The max date can not exceed today's date because we're adding only existing movies
        max_date = datetime.now().date()
        # Existing_date, existing_title checks for matches in the model compared to users form data input
        existing_date = query_movie_filter_date_exists(form_date)
        # Needs to convert the title from the from-input to upper letters to make the check for existence in the DB
        # this is required because all str data is written as upper() in the DB
        existing_title = query_movie_filter_title_exists(from_title.upper())
        if (form_date < min_date) or (form_date > max_date):
            raise ValidationError(f"Release date must be within the range {min_date} to today's date -{max_date}")
        # If user attempt to add movie which contains title and release date that's already exist in the model it
        # raise an exception. After research, I noticed there exist movies with exactly the same names,
        # but are released on different dates. My solution for this case is to prevent adding movies with same titles
        # and with exactly the same release date. Same titles are allowed, but with different realise date
        elif existing_title and existing_date:
            raise ValidationError(f"A movie {from_title.upper()} released on {form_date} already exist."
                                  f" Same movie titles are allowed but with different release dates")
        return form_date

    class Meta:
        model = Movie
        # Fields added in the list will be displayed in the add movie form
        fields = ["title", "description", "release_date", "director", "gener", "cover"]


class FavoritesMovieForm(forms.Form):
    # Creates a query set of all movies presented as a list in the HTML allowing the user to select a movie
    movie = queryset_movie_form(forms.ModelChoiceField)


# Using the Django built-in User model as a form of registration inheriting all its rules and restrictions
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        # password2 is for password conformation
        fields = ["username", "password1", "password2"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
