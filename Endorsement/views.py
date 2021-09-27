from rest_framework import generics
from Endorsement.serializers import *
from Endorsement.models import Endorsement,EndorsementRequest
from rest_framework.pagination import LimitOffsetPagination
# Create your views here.

#List and create an event object
class EndorsementCreateApiView(generics.CreateAPIView):
    queryset = Endorsement.objects.all()
    serializer_class = EndorsementSerializer

# Retreive,Update and Delete a event object 
class EndorsementDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Endorsement.objects.all()
    serializer_class = EndorsementSerializer

class EndorsementRequestCreateView(generics.CreateAPIView):
    queryset = EndorsementRequest.objects.all()
    serializer_class = EndorsementRequestSerializer

class EndorsementRequestDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EndorsementRequest.objects.all()
    serializer_class = EndorsementRequestSerializer


class TribesEndorsementListAPIView(generics.ListAPIView):
    serializer_class = EndorsementSerializer
    pagination_class = LimitOffsetPagination
    def get_queryset(self):
        tribeleaderId = self.kwargs.get('tribeleaderId')
        return Endorsement.objects.filter(user = tribeleaderId).order_by('-updated_at')

class BrandEndorsementListAPIView(generics.ListAPIView):
    serializer_class = EndorsementSerializer
    pagination_class = LimitOffsetPagination
    def get_queryset(self):
        brandId = self.kwargs.get('brandId')
        return Endorsement.objects.filter(brand = brandId).order_by('-updated_at')

class UserEndorsementRequestListAPIView(generics.ListAPIView):
    serializer_class = EndorsementRequestSerializer
    pagination_class = LimitOffsetPagination
    def get_queryset(self):
        UserId = self.kwargs.get('userId')
        return EndorsementRequest.objects.filter(user = UserId).order_by('-updated_at')

# class BrandEndorsementRequestListAPIView(generics.ListAPIView):
#     serializer_class = EndorsementRequestSerializer
#     pagination_class = LimitOffsetPagination
#     def get_queryset(self):
#         brandId = self.kwargs.get('brandId')
#         return EndorsementRequest.objects.filter(brand = brandId).order_by('-updated_at')
