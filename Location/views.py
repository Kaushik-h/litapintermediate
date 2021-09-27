
from rest_framework import generics
from Location.serializers import PhysicalLocationSerializer
from Location.models import PhysicalLocation
from rest_framework.response import Response

class PhysicalLocationListCreateApiView(generics.ListCreateAPIView):
    queryset = PhysicalLocation.objects.all()
    serializer_class = PhysicalLocationSerializer

class PhysicalLocationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PhysicalLocation.objects.all()
    serializer_class = PhysicalLocationSerializer