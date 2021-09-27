from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from Order.serializers import *
from Order.models import *
# Create your views here.
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination


class OrderCreateApiView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = LimitOffsetPagination
    def get_queryset(self):
        return Order.objects.filter(owner = self.request.user).order_by('-created_at')

class OrderListApiView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    pagination_class = LimitOffsetPagination
    def get_queryset(self):
        return Order.objects.filter(owner = self.request.user).order_by('-created_at')
# Retreive,Update and Delete a event object 
class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class cartDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return Cart.objects.get_or_create(owner=self.request.user)[0]