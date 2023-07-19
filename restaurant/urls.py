from django.urls import path
from restaurant import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='tables')