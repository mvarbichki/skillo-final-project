from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError
from .models import Movie
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput


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
    # Adds calendar widget
    release_year = forms.DateField(
        label="Release date *",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
    )
    cover = forms.ImageField(
        label="Cover image",
        required=False
    )

    def clean_release_year(self):
        # All values are in date() format so they can be compared to each other
        form_date = self.cleaned_data['release_year']
        # Restricting user input date. Minimum date is 1895-12-28 (release date of the first movie)
        min_date = datetime(1895, 12, 28).date()
        # The max date can not exceed today's date because we're adding only existing movies
        max_date = datetime.now().date()
        if (form_date < min_date) or (form_date > max_date):
            raise ValidationError(f"Release date must be within the range {min_date} to today's date({max_date})")
        return form_date

    class Meta:
        model = Movie
        # Fields added in the list will be displayed in the add movie form
        fields = ["title", "description", "release_year", "director", "gener", "cover"]


# Using Django build-in User model as form of registration
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        # password2 is for password conformation
        fields = ["username", "password1", "password2"]


class LoginForm(AuthenticationForm):
    # Pass widgets as arguments to user and pass
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
