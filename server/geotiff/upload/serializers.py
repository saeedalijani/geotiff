from rest_framework import serializers
from .models import GeoTiff


class GeoTiffSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeoTiff
        fields = ('source_file', )
