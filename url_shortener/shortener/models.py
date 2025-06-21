import random

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

    @staticmethod
    def _generate_shortened_url():
        """
        Generate a random shortened URL.
        """
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        shortened_url = "".join(random.choice(characters) for _ in range(10))
        return shortened_url

    def save(self, *args, **kwargs):
        """
        Override save method to generate a unique shortened URL.
        """
        if not self.shortened_url:
            self.shortened_url = self._generate_shortened_url()
            while ShortenedURL.objects.filter(
                shortened_url=self.shortened_url
            ).exists():
                self.shortened_url = self._generate_shortened_url()
        super().save(*args, **kwargs)
