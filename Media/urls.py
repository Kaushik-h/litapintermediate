from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Media.views import *

urlpatterns = [
    
     path('media',MediaListApiView.as_view()),
     path('media/<pk>',MediaDetailAPIView.as_view())
     
]