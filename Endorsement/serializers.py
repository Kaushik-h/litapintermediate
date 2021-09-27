from rest_framework import serializers
from Endorsement.models import Endorsement,EndorsementRequest
from MediaCollection.serializers import MediaCollectionSerializer
from MediaCollection.models import MediaCollection

class EndorsementSerializer(serializers.ModelSerializer):
    
    advertisementCollections = MediaCollectionSerializer()

    def create(self, validated_data):
        advertisementCollections_data = validated_data.pop('advertisementCollections')

        advertisementMedia = advertisementCollections_data.pop('media')
        advertisementCollections = MediaCollection.objects.create(**advertisementCollections_data)
        advertisementCollections.media.set(advertisementMedia)
        
        commodities = validated_data.pop('commodities')
        

        endorsement = Endorsement.objects.create(advertisementCollections=advertisementCollections,**validated_data)
        endorsement.commodities.set(commodities)
        
        return endorsement
    
    def update(self, instance, validated_data):
        
        advertisementCollections_data = validated_data.pop('advertisementCollections')
        
        for item in validated_data:
            if Endorsement._meta.get_field(item):
                setattr(instance, item, validated_data[item])

        instance.advertisementCollections.delete()
        advertisementMedia = advertisementCollections_data.pop('media')
        advertisementCollections = MediaCollection.objects.create(**advertisementCollections_data)
        advertisementCollections.media.set(advertisementMedia)
        instance.advertisementCollections = advertisementCollections        

        instance.save()
        
        return instance

    class Meta:
        model=Endorsement
        fields ='__all__'

class EndorsementRequestSerializer(serializers.ModelSerializer):
    collection = MediaCollectionSerializer()
    endorsement = EndorsementSerializer()

    def create(self, validated_data):
        collection_data = validated_data.pop('collection')
        endorsement_data = validated_data.pop('endorsement')
        collectionMedia = collection_data.pop('media')
        collection = MediaCollection.objects.create(**collection_data)
        collection.media.set(collectionMedia)
        endorsement = Endorsement.objects.create(**endorsement_data)
        endorsementRequest = EndorsementRequest.objects.create(endorsement=endorsement,collection=collection,**validated_data)
        return endorsementRequest
    
    def update(self, instance, validated_data):
        
        collection_data = validated_data.pop('collection')
        endorsement_data = validated_data.pop('endorsement')
        
        for item in validated_data:
            if EndorsementRequest._meta.get_field(item):
                setattr(instance, item, validated_data[item])
        
        endorsement = instance.endorsement
        for item in endorsement_data:
            if Endorsement._meta.get_feild(item):
                setattr(endorsement, item, endorsement_data[item])

        instance.collection.delete()
        collectionMedia = collection_data.pop('media')
        collection = MediaCollection.objects.create(**collection_data)
        collection.media.set(collectionMedia)
        instance.collection = collection        

        instance.save()
        
        return instance

    class Meta:
        model=EndorsementRequest
        fields ='__all__'
