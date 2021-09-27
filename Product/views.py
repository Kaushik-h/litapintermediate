from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics
from Product.serializers import *
from Product.models import Product,Commodity
# Create your views here.
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

#List and create an event object
class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = LimitOffsetPagination

class ProductAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LimitOffsetPagination

# Retreive,Update and Delete a event object 
class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class TribeProductListAPIView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    def get_queryset(self):
        tribeleaderId = self.kwargs.get('tribeleaderId')
        return Product.objects.filter(owner = tribeleaderId).order_by('-updated_at')

class TribesProductListAPIView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    def get_queryset(self):
        tribeLeaderIdList = self.request.GET.getlist('tribeleaderlist')
        return Product.objects.filter(owner__in = tribeLeaderIdList).order_by('-updated_at')

class CommodityAPIView(generics.CreateAPIView):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer


class TribesCommodityListAPIView(generics.ListAPIView):
    serializer_class = CommoditySerializer
    def get_queryset(self):
        tribeLeaderId = self.kwargs('tribeleaderId')
        return Commodity.objects.filter(owner = tribeLeaderId).order_by('-updated_at')

class BrandCommodityListAPIView(generics.ListAPIView):
    serializer_class = CommoditySerializer
    def get_queryset(self):
        brandId = self.kwargs('brandId')
        return Commodity.objects.filter(brand = brandId).order_by('-updated_at')

