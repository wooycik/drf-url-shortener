from rest_framework import serializers
from django.urls import reverse

from .models import ShortenedURL


class ShortenedURLSerializer(serializers.ModelSerializer):
    shortened_url = serializers.SerializerMethodField()

    class Meta:
        model = ShortenedURL
        fields = ["original_url", "shortened_url"]
        read_only_fields = ["shortened_url"]

    def validate_original_url(self, value):
        """
        Validate that the original URL is a valid URL.
        """
        if not value.startswith(("http://", "https://")):
            raise serializers.ValidationError(
                "Original URL must start with http:// or https://"
            )
        return value

    def get_shortened_url(self, obj):
        """
        Return the shortened URL.
        """
        relative_url = reverse(
            "retrieve_shortened_url", kwargs={"shortened_url": obj.shortened_url}
        )
        request = self.context.get("request")
        if request:
            return request.build_absolute_uri(relative_url)
        return relative_url
