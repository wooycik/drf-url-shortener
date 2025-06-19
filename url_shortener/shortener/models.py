from django.db import models


class ShortenedURL(models.Model):
    """
    Model to store original URLs and their shortened versions.
    """

    original_url = models.URLField(max_length=2048, unique=True)
    shortened_url = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["shortened_url"]),
        ]

    def __str__(self):
        return f"{self.original_url} -> {self.shortened_url}"

    def create_shortened_url(self, original_url):
        """
        Method to generate a shortened URL.

        Args:
            original_url (str): The original URL to shorten.
        """
        pass
