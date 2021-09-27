from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Order.views import *

urlpatterns = [
    
     path('orders/',OrderListApiView.as_view()),
     path('order',OrderCreateApiView.as_view()),
     path('order/<pk>',OrderDetailAPIView.as_view()),
     path('cart',cartDetailAPIView.as_view())
     
]