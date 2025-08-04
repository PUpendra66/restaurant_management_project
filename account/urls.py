from django.urls import path
from .views import *

urlpatterns = [
    path('api/restaurant/<int:pk>/menu/',RestaurantMenuAPIView.as_view(),name='restaurant-menu'),
]