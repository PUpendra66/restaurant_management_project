from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurant


# Create your views here.

class RestaurantMenuAPIView(APIView):

    """ 
    Retrive the hardcoded menu for a restaurant by ID.

    """
    def get(self,request,pk):
        try:
            restaurant=Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist():
            return Response({'error':'Restaurant not found'},status=status.HTTP_404_NOT_FOUND)
        menu_data=[
            {
            "dish_name":"Margherita Pizza",
            "description":"Classic cheeze and tomoto pizza",
            "price":299
            },
            {
                "dish_name":"Chicken Tikka",
                "description":"Spicy grilled chicken cubes",
                "price":399
            },
            {"dish_name":"pasta alfredo",
            "description":"creamy white sauce pasta",
            "price":299}
        ]

        return Response({"restaurant":restaurant.name,
        "menu":menu_data})

