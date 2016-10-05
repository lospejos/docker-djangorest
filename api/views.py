from models import Hotel, Client, Stay
from rest_framework import viewsets
from api.serializers import ClientSerializer, HotelSerializer, StaySerializer


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hotel's clients to be viewed or edited.
    """
    queryset = Client.objects.all().order_by('-created')
    serializer_class = ClientSerializer


class HotelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class StayViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Stay.objects.all()
    serializer_class = StaySerializer