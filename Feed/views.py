from rest_framework import generics
from Feed.serializers import *
from Feed.models import Feed
from rest_framework.pagination import LimitOffsetPagination
# Create your views here.

#List and create an event object
class FeedListApiView(generics.ListCreateAPIView):
    serializer_class = FeedSerializer
    queryset = Feed.objects.all()
   

class UserFeedListApiView(generics.ListAPIView):
    serializer_class = FeedSerializer
    pagination_class = LimitOffsetPagination
    def get_queryset(self):
        writer = self.kwargs.get('writerId')
        return Feed.objects.filter(writer = writer).order_by('-updated_at')

# Retreive,Update and Delete a event object 
class FeedDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer


class TribesFeedsListAPIView(generics.ListAPIView):
    serializer_class = FeedSerializer
    def get_queryset(self):
        tribeLeaderIdList = self.request.GET.getlist('tribeleaderlist')
        return Feed.objects.filter(writer__in = tribeLeaderIdList).order_by('-updated_at')


