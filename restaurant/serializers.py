from rest_framework import serializers
from restaurant.models import Menu, Booking


#Create menu serializer
class MenuSerializer(serializers.Serializer):
    class Meta:
        model = Menu
        fields = "__all__"


#Create booking serializer
class BookingSerializer(serializers.Serializer):
    class Meta:
        model = Booking
        fields = "__all__"