from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Brand.views import *

urlpatterns = [
    
     path('brand/',BrandCreateApiView.as_view()),
     path('brand/<pk>',BrandDetailAPIView.as_view())
     
]