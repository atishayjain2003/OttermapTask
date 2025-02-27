from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Vendorshop

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']    
class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendorshop
        fields =  ['id','Shopname', 'Businesstype', 'Latitude', 'Longitude']