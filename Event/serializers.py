from rest_framework import serializers
from Event.models import Event

from Auth.serializers import UserNameSerializer
from MediaCollection.serializers import MediaCollectionSerializer,MediaCollectionListSerializer
from Location.serializers import PhysicalLocationSerializer
from MediaCollection.models import MediaCollection
from Location.models import PhysicalLocation

class EventSerializer(serializers.ModelSerializer):
    mediaCollection = MediaCollectionSerializer(required=False)
    location = PhysicalLocationSerializer(required=False)
    def create(self, validated_data):
        mediaCollection_data = validated_data.pop('mediaCollection',None)
        location_data = validated_data.pop('location',None)
        
        if mediaCollection_data :
            media = mediaCollection_data.pop('media')
            mediaCollection = MediaCollection.objects.create(**mediaCollection_data)
            mediaCollection.media.set(media)
        else:
            mediaCollection = None

        location = PhysicalLocation.objects.create(**location_data) if location_data else None

        event = Event.objects.create(location=location,mediaCollection=mediaCollection,**validated_data)
        return event
    
    def update(self, instance, validated_data):

        mediaCollection_data = validated_data.pop('mediaCollection',None)
        location_data = validated_data.pop('location',None)
        
        for item in validated_data:
            if Event._meta.get_field(item):
                setattr(instance, item, validated_data[item])
        if instance.mediaCollection:
            instance.mediaCollection.delete()
        if mediaCollection_data:
            media = mediaCollection_data.pop('media',None)
            mediaCollection = MediaCollection.objects.create(**mediaCollection_data)
            mediaCollection.media.set(media)
            instance.mediaCollection = mediaCollection

        if instance.location:
            instance.location.delete()
        if location_data:
            location = PhysicalLocation.objects.create(**location_data)
            instance.location = location

        instance.save()
        return instance
    class Meta:
        model=Event
        fields='__all__'

class EventListSerializer(serializers.ModelSerializer):
    organizer = UserNameSerializer()
    mediaCollection = MediaCollectionListSerializer(required=False)
    participants = UserNameSerializer(many=True)
    class Meta:
        model=Event
        fields='__all__'