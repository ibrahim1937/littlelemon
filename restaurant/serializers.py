from rest_framework import serializers
from restaurant.models import Menu, Booking


#Create menu serializer
class MenuSerializer(serializers.Serializer):
    class Meta:
        model = Menu
        fields = "__all__"
    
    def create(self, validated_data):
        return Menu.objects.create(**validated_data)


#Create booking serializer
class BookingSerializer(serializers.Serializer):
    class Meta:
        model = Booking
        fields = "__all__"