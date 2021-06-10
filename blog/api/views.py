from blog.models import Destination
from blog.api.serializers import DestinationSerializer
from rest_framework import viewsets


class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
