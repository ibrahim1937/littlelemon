from django.shortcuts import render
from restaurant.serializers import MenuSerializer, BookingSerializer
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, RetrieveUpdateAPIView
from restaurant.models import Menu, Booking
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class MenuItemView(ListCreateAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        return Menu.objects.all()
    
class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        return Menu.objects.all()
    
class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer

    def get_queryset(self):
        return Booking.objects.all()