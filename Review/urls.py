from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Review.views import *

urlpatterns = [
    
     path('reviews/',ReviewListApiView.as_view()),
     path('reviews/<pk>',ReviewDetailAPIView.as_view())
     
]