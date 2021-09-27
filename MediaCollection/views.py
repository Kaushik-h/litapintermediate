
from rest_framework import generics
from MediaCollection.serializers import MediaCollectionSerializer
from MediaCollection.models import MediaCollection
# Create your views here.

#List and create an event object
class MediaCollectionListApiView(generics.ListCreateAPIView):
    queryset = MediaCollection.objects.all()
    serializer_class = MediaCollectionSerializer

# Retreive,Update and Delete a event object 
class MediaCollectionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MediaCollection.objects.all()
    serializer_class = MediaCollectionSerializer

