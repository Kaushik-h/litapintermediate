from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Location.views import *

urlpatterns = [
    
     path('location/',PhysicalLocationListCreateApiView.as_view()),
     path('location/<pk>',PhysicalLocationDetailAPIView.as_view()),  
]