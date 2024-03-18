from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError
from .models import Movie


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
    # adds calendar widget
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

    # Restricting user input date. Minimum date could be 1895-12-28 (release date of teh first movie). Max date is today
    def clean_release_year(self):
        form_date = self.cleaned_data['release_year']
        min_date = datetime(1895, 12, 28).date()
        max_date = datetime.now().date()

        if form_date < min_date or form_date > max_date:
            raise ValidationError(f"Date must be within the range {min_date} to {max_date}")
        return form_date

    class Meta:
        model = Movie
        # fields to be displayed in add movie form
        fields = ["title", "description", "release_year", "director", "gener", "cover"]
