from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from Profile.serializers import *
from Profile.models import KYC,Tribe
from Auth.models import User
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
# Create your views here.

#List and create an event object
class UserListApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Retreive,Update and Delete a event object 
class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#List and create an Tribe object
class TribeCreateApiView(generics.CreateAPIView):
    queryset = Tribe.objects.all()
    serializer_class = TribeSerializer

# Retreive,Update and Delete a Tribe object 
class TribeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tribe.objects.all()
    serializer_class = TribeSerializer

class FollowingTribesListAPIView(generics.ListAPIView):
    serializer_class = TribeSerializer
    pagination_class = LimitOffsetPagination
    def get_queryset(self):
        return Tribe.objects.filter(fans = self.request.user)

#List and create an Tribe object
class KYCListApiView(generics.CreateAPIView):
    queryset = KYC.objects.all()
    serializer_class = KYCSerializer

# Retreive,Update and Delete a Tribe object 
class KYCDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KYC.objects.all()
    serializer_class = KYCSerializer

class UserBioApiView(generics.RetrieveAPIView):
    serializer_class = BioSerializer
    def get_object(self):
        userId = self.kwargs.get('userId')
        bio = get_object_or_404(Bio,user = userId)
        return bio


        