from rest_framework import serializers
from MediaCollection.models import MediaCollection
from Media.models import Media
from Media.serializers import MediaSerializer
class MediaCollectionSerializer(serializers.ModelSerializer):
    media = serializers.PrimaryKeyRelatedField(queryset=Media.objects.all(),many=True)
    class Meta:
        model=MediaCollection
        fields='__all__'
        extra_kwargs = {
            'collectionId': {'validators': []},
        }

class MediaCollectionListSerializer(serializers.ModelSerializer):
    media = MediaSerializer(many=True)
    class Meta:
        model=MediaCollection
        fields='__all__'