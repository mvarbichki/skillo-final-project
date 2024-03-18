from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.listing_page, name="listing_page"),
    path("details_page/<int:movie_id>", views.details_page, name="details_page"),
    path("search_page", views.search_page, name="search_page"),
    path("add_movie_page", views.add_movie_page, name="add_movie_page")
]

# Serv the static files/covers img
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
