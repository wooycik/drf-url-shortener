from django.urls import path
from .views import ShortenerViewSet

urlpatterns = [
    path("", ShortenerViewSet.as_view(), name="shorten_url"),
    path(
        "<str:shortened_url>/",
        ShortenerViewSet.as_view(),
        name="retrieve_shortened_url",
    ),
]
