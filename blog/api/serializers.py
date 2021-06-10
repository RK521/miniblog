from blog.models import Destination
from rest_framework import serializers


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['id', 'title', 'desc']