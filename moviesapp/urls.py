from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.listing_page, name="listing_page"),
    path("details_page/<int:movie_id>", views.details_page, name="details_page"),
    path("search_page", views.search_page, name="search_page"),
    path("add_movie_page", views.add_movie_page, name="add_movie_page"),
    path("register", views.register, name="register"),
    path("user_login", views.user_login, name="user_login"),
    path("user_logout", views.user_logout, name="user_logout"),
    path("add_favorites_page", views.add_favorites_page, name="add_favorites_page"),
    path("show_favorites_page", views.show_favorites_page, name="show_favorites_page"),
    path("remove_favorites_page/<int:favorite_id>", views.remove_favorites_page, name="remove_favorites_page")
]

# Serv the static files/covers img
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
