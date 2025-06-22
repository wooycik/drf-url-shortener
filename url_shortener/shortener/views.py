from rest_framework import status, generics
from rest_framework.response import Response

from .models import ShortenedURL
from .serializers import ShortenedURLSerializer


class ShortenerUrlCreateViewSet(generics.CreateAPIView):
    """
    ViewSet for handling URL shortening and retrieval.
    """

    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer
    authentication_classes = []
    permission_classes = []

    def create(self, request, *args, **kwargs):
        # Check for existing URL first, before validation
        original_url = request.data.get("original_url")
        if original_url:
            existing_url = ShortenedURL.objects.filter(
                original_url=original_url
            ).first()
            if existing_url:
                return Response(
                    self.get_serializer(existing_url).data,
                    status=status.HTTP_201_CREATED,
                )

        # Proceed with normal creation if no existing URL found
        return super().create(request, *args, **kwargs)


class ShortenedURLRetrieveViewSet(generics.RetrieveAPIView):
    """
    ViewSet for retrieving a shortened URL.
    """

    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer
    authentication_classes = []
    permission_classes = []
    lookup_field = "shortened_url"

    def get(self, request, *args, **kwargs):
        if self.lookup_field in kwargs:
            return super().retrieve(request, *args, **kwargs)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
