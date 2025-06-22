from django.urls import path
from .views import ShortenerUrlCreateViewSet

urlpatterns = [
    path("", ShortenerUrlCreateViewSet.as_view(), name="shorten_url"),
]
