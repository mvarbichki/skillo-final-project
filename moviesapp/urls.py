from django.urls import path
from . import views

urlpatterns = [
    path("", views.listing_page, name="listing_page"),
    path("details_page/<int:movie_id>", views.details_page, name="details_page")
]