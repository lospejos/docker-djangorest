from models import Client, Hotel, Stay
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'work')


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'name', 'address', 'website', 'rating')


class StaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stay
        fields = ('cilent', 'hotel', 'room', 'check_in', 'check_out')

