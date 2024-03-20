from django.contrib import admin
from .models import Movie, Favorites

# Register your models here.
admin.site.register(Movie)
admin.site.register(Favorites)