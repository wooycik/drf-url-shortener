import pytest

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import ShortenedURL


@pytest.fixture
def api_client():
    """API client fixture."""
    return APIClient()


@pytest.mark.django_db
class TestShortenerViewSet:
    """Tests for the ShortenerViewSet."""

    def test_create_shortened_url_http(self, api_client):
        """Test creating a shortened URL."""
        url = "http://example.com"
        response = api_client.post(
            reverse("shorten_url"), data={"original_url": url}, format="json"
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert "shortened_url" in response.data
        assert ShortenedURL.objects.filter(original_url=url).exists()

    def test_create_shortened_url_https(self, api_client):
        """Test creating a shortened URL."""
        url = "https://example.com"
        response = api_client.post(
            reverse("shorten_url"), data={"original_url": url}, format="json"
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert "shortened_url" in response.data
        assert ShortenedURL.objects.filter(original_url=url).exists()

    def test_create_shortened_url_without_protocol(self, api_client):
        """Test creating a shortened URL."""
        url = "example.com"
        response = api_client.post(
            reverse("shorten_url"), data={"original_url": url}, format="json"
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "original_url" in response.data
        assert not ShortenedURL.objects.filter(original_url=url).exists()

    def test_create_existing_shortened_url(self, api_client):
        """Test creating an existing shortened URL."""
        original_url = "http://example.com"
        ShortenedURL.objects.create(original_url=original_url)
        response = api_client.post(
            reverse("shorten_url"), data={"original_url": original_url}, format="json"
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert "shortened_url" in response.data

    def test_retrieve_shortened_url(self, api_client):
        """Test retrieving a shortened URL."""
        original_url = "http://example.com"
        shortened_url_instance = ShortenedURL.objects.create(original_url=original_url)
        response = api_client.get(
            reverse(
                "retrieve_shortened_url",
                kwargs={"shortened_url": shortened_url_instance.shortened_url},
            )
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data["original_url"] == original_url

    def test_retrieve_nonexistent_shortened_url(self, api_client):
        """Test retrieving a nonexistent shortened URL."""
        response = api_client.get(
            reverse("retrieve_shortened_url", kwargs={"shortened_url": "nonexistent"})
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_retrieve_shortened_url_with_invalid_method(self, api_client):
        """Test retrieving a shortened URL with an invalid method."""
        original_url = "http://example.com"
        shortened_url_instance = ShortenedURL.objects.create(original_url=original_url)
        response = api_client.post(
            reverse(
                "retrieve_shortened_url",
                kwargs={"shortened_url": shortened_url_instance.shortened_url},
            )
        )
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
