from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Feed.views import *

urlpatterns = [
    
     path('feed/',FeedListApiView.as_view()),
     path('feed/<pk>',FeedDetailAPIView.as_view()),
     path('feed/userfeed/<writerId>',UserFeedListApiView.as_view()),
     path('feed/feedlist/feedbytribeleaders',TribesFeedsListAPIView.as_view())
     
]