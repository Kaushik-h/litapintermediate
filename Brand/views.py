from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from Brand.serializers import *
from Brand.models import Brand

class BrandCreateApiView(generics.CreateAPIView):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

# Retreive,Update and Delete a event object 
class BrandDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer