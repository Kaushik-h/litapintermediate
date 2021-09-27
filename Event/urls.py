from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Event.views import *

urlpatterns = [
    
     path('event',EventCreateApiView.as_view()),
     path('event/<pk>',EventDetailAPIView.as_view()),
     path('events',EventListApiView.as_view()),
     path('events/organizing/<tribeleaderId>',TribeEventListAPIView.as_view()),
     path('events/organizing/tribelist',TribesEventListAPIView.as_view()),
     path('events/participating',ParticipantEventListAPIView.as_view()),
     path('events/participateevent',ParticipateEventAPIView.as_view()),
]