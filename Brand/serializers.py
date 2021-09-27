from rest_framework import serializers
from Brand.models import Brand
from MediaCollection.serializers import MediaCollectionSerializer
from MediaCollection.models import MediaCollection

class BrandSerializer(serializers.ModelSerializer):
    logoCollections = MediaCollectionSerializer()
    advertisementCollections = MediaCollectionSerializer()

    def create(self, validated_data):
        logoCollections_data = validated_data.pop('logoCollections')
        advertisementCollections_data = validated_data.pop('advertisementCollections')
        
        logoMedia = logoCollections_data.pop('media')
        logoCollections = MediaCollection.objects.create(**logoCollections_data)
        logoCollections.media.set(logoMedia)

        advertisementMedia = advertisementCollections_data.pop('media')
        advertisementCollections = MediaCollection.objects.create(**advertisementCollections_data)
        advertisementCollections.media.set(advertisementMedia)

        brand = Brand.objects.create(logoCollections = logoCollections,advertisementCollections=advertisementCollections,**validated_data)
        return brand
    
    def update(self, instance, validated_data):
        
        logoCollections_data = validated_data.pop('logoCollections')
        advertisementCollections_data = validated_data.pop('advertisementCollections')
        
        for item in validated_data:
            if Brand._meta.get_field(item):
                setattr(instance, item, validated_data[item])
        

        instance.logoCollections.delete()
        logoMedia = logoCollections_data.pop('media')
        logoCollections = MediaCollection.objects.create(**logoCollections_data)
        logoCollections.media.set(logoMedia)
        instance.logoCollections = logoCollections

        instance.advertisementCollections.delete()
        advertisementMedia = advertisementCollections_data.pop('media')
        advertisementCollections = MediaCollection.objects.create(**advertisementCollections_data)
        advertisementCollections.media.set(advertisementMedia)
        instance.advertisementCollections = advertisementCollections        

        instance.save()
        
        return instance
    class Meta:
        model=Brand
        exclude = ['deleted_at']