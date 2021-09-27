from rest_framework import serializers
from Feed.models import Feed
from MediaCollection.serializers import MediaCollectionSerializer
from MediaCollection.models import MediaCollection

class FeedSerializer(serializers.ModelSerializer):
    mediaCollection = MediaCollectionSerializer()

    def create(self, validated_data):
        mediaCollection_data = validated_data.pop('mediaCollection',None)

        if mediaCollection_data:
            media = mediaCollection_data.pop('media')
            mediaCollection = MediaCollection.objects.create(**mediaCollection_data)
            mediaCollection.media.set(media)
        else:
            mediaCollection = None

        feed = Feed.objects.create(mediaCollection=mediaCollection,**validated_data)
        return feed
    
    def update(self, instance, validated_data):

        mediaCollection_data = validated_data.pop('mediaCollection',None)
        
        for item in validated_data:
            if Feed._meta.get_field(item):
                setattr(instance, item, validated_data[item])
        
        if instance.mediaCollection:
            instance.mediaCollection.delete()
        if mediaCollection_data:
            media = mediaCollection_data.pop('media')
            mediaCollection = MediaCollection.objects.create(**mediaCollection_data)
            mediaCollection.media.set(media)
            instance.mediaCollection = mediaCollection

        instance.save()
        return instance
    class Meta:
        model=Feed
        fields='__all__'