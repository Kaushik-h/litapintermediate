from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Endorsement.views import *

urlpatterns = [
    
     path('endorsement/',EndorsementCreateApiView.as_view()),
     path('endorsement/<pk>',EndorsementDetailAPIView.as_view()),
     path('endorsements/tribe/<tribeleaderId>',TribesEndorsementListAPIView.as_view()),
     path('endorsements/brand/<brandId>',BrandEndorsementListAPIView.as_view()),

     path('endorsementrequest/',EndorsementRequestCreateView.as_view()),
     path('endorsementrequest/<pk>',EndorsementDetailAPIView.as_view()),
     path('endorsementrequests/user/<userId>',UserEndorsementRequestListAPIView.as_view()),
     
]
