from django.shortcuts import render
from rest_framework import generics
from Review.serializers import *
from Review.models import Review
# Create your views here.

#List and create an event object
class ReviewListApiView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Retreive,Update and Delete a event object 
class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class =ReviewSerializer
