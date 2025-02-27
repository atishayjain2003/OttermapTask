from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from .models import Vendorshop
from .serializers import ShopSerializer
from django.shortcuts import get_object_or_404
from geopy.distance import geodesic


class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email=request.data.get('email')

        if not username or not password or not email:
            return Response({'error': 'Please provide, username, password and email'})

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'})

        user = User.objects.create_user(username=username, password=password, email=email)
        token, _ = Token.objects.get_or_create(user=user)

        return Response({'message': 'The user has been created successfully', 'token': token.key})

class RegisterShopView(generics.ListCreateAPIView):
    queryset=Vendorshop.objects.all()
    serializer_class=ShopSerializer
    permission_classes = [IsAuthenticated]
    #ensuring that user creates only his/her shop
    def get_queryset(self):
        return Vendorshop.objects.filter(Owner=self.request.user)
    def perform_create(self, serializer):
        serializer.save(Owner=self.request.user)

class ShopDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=ShopSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Vendorshop.objects.filter(Owner=self.request.user)
    def delete(self, request, *args, **kwargs):
        shop = get_object_or_404(Vendorshop, id=kwargs['pk'], Owner=request.user)
        shop.delete()
        return Response({'message': 'Shop deleted successfully'})

class NearbyShopsView(APIView):
    permission_classes = [AllowAny]

    
    def post(self, request):
        data = request.data  # Read JSON body
        lat = data.get("latitude")
        lon = data.get("longitude")
        radius = data.get("radius", 5)  # Default to 5 km

        # Validate input
        if not lat or not lon:
            return Response({"error": "latitude and longitude are required"}, status=400)

        try:
            lat = float(lat)
            lon = float(lon)
            radius = float(radius)
        except ValueError:
            return Response({"error": "latitude, longitude, and radius must be valid numbers"}, status=400)

        # Get nearby shops
        nearby_shops = []
        for shop in Vendorshop.objects.all():
            if shop.Latitude is not None and shop.Longitude is not None:
                shop_distance = geodesic((lat, lon), (shop.Latitude, shop.Longitude)).km
                if shop_distance <= radius:
                    nearby_shops.append(ShopSerializer(shop).data)

        return Response(nearby_shops)