from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from .models import Vendorshop
from .serializers import ShopSerializer

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
