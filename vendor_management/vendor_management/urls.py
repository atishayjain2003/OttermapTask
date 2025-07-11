"""
URL configuration for vendor_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop.views import RegisterUserView, RegisterShopView, ShopDetailView, NearbyShopsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', RegisterUserView.as_view()),
    path('shops/', RegisterShopView.as_view()),
    path('shops/<int:pk>/', ShopDetailView.as_view()),
    path('nearby-shops/', NearbyShopsView.as_view()),
]
