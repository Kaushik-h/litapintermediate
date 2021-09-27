from django.shortcuts import render
from rest_framework import generics
from Media.models import Media
from Media.serializers import MediaSerializer

# Create your views here.

class MediaListApiView(generics.ListCreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

# Retreive,Update and Delete a event object 
class MediaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
