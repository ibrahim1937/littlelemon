from django.shortcuts import render
from restaurant.serializers import MenuSerializer, BookingSerializer
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, RetrieveUpdateAPIView

# Create your views here.
#MenuItemView – inheriting the rest_framework.generics.ListCreateView class. It handles the POST and GET method calls.
class MenuItemView(ListCreateAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        return Menu.objects.all()


#SingleMenuItemView – inherits the RetrieveUpdateAPIView and DestroyAPIView classes both imported from the rest_framework.generics module. This class is responsible for processing GET, PUT and DELETE method calls.

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        return Menu.objects.all()