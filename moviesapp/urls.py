from django.urls import path
from . import views

urlpatterns = [
    path("", views.listing_page, name="main_page")
]