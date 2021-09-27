from django.urls import path
from django.conf.urls import url
from Profile.views import *

urlpatterns = [
    
     path('users/',UserListApiView.as_view()),
     path('users/<pk>',UserDetailAPIView.as_view()),

     path('tribe/',TribeCreateApiView.as_view()),
     path('tribe/<pk>',TribeDetailAPIView.as_view()),
     path('tribes/following',FollowingTribesListAPIView.as_view()),

     path('bio/<userId>',UserBioApiView.as_view()),

     path('kyc/',KYCListApiView.as_view()),
     path('kyc/<pk>',KYCDetailAPIView.as_view())
     
]