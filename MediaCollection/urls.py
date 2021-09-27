from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from MediaCollection.views import *

urlpatterns = [
    
     path('mediacollection/',MediaCollectionListApiView.as_view()),
     path('mediacollection/<pk>',MediaCollectionDetailAPIView.as_view())
     
]