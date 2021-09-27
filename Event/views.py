from django.shortcuts import render

# Create your views here.
from rest_framework import generics,status
from Event.serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from django.shortcuts import get_object_or_404

from Event.models import Event
from Profile.models import Tribe
from rest_framework.pagination import LimitOffsetPagination
from litap.utils import sendResponse
# Create your views here.

#List and create an event object
class EventListApiView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer

class EventCreateApiView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# Retreive,Update and Delete a event object 
class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class TribeEventListAPIView(APIView):
    serializer_class = EventSerializer
    pagination_class = LimitOffsetPagination
    def get_queryset(self):
        currentTime = datetime.now()
        tribeleaderId = self.kwargs.get('tribeleaderId')
        return Event.objects.filter(organizer = tribeleaderId , eventTimeStamp__gte = currentTime).order_by('created_at')

class ParticipantEventListAPIView(generics.ListAPIView):

    serializer_class = EventSerializer
    pagination_class = LimitOffsetPagination
    def get_queryset(self):
        return Event.objects.filter(participants = self.request.user).order_by('created_at')


class TribesEventListAPIView(generics.ListAPIView):
    serializer_class = EventSerializer
    def get_queryset(self):
        tribeLeaderIdList = self.request.GET.getlist('tribeleaderlist')
        return Event.objects.filter(organizer__in = tribeLeaderIdList).order_by('-updated_at')

class ParticipateEventAPIView(APIView):
    serializer_class = EventSerializer
    def post(self,request):
        user = request.user
        eventId = request.data.get('eventId')
        event = get_object_or_404(Event,eventId = eventId)
        if event.maxParticipants > event.participants.all().count():
            event.participants.add(user)
            return sendResponse(True,status.HTTP_202_ACCEPTED)
        return sendResponse(False,status.HTTP_403_FORBIDDEN,None,"MaxParticipants")

