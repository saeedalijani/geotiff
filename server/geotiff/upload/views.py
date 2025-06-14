from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import GeoTiffSerializer
from .models import GeoTiff


class GeoTiffListCreateView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = GeoTiffSerializer
    queryset = GeoTiff.objects.all()
