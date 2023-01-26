from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_listing, name="create"),
    path("listing/<int:listing_id>", views.listing_view, name="listing_view"),
    path("watchlist", views.watchlist_view, name="watchlist_view"),
    path("<int:listing_id>", views.watchlist_add, name="watchlist_add")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)