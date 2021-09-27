from rest_framework import serializers
from Product.models import *
from MediaCollection.serializers import MediaCollectionSerializer,MediaCollectionListSerializer
from Brand.serializers import BrandSerializer
from MediaCollection.models import MediaCollection

class CustomizationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomizationType
        fields='__all__'

class DimensionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dimension
        fields='__all__'

class CommoditySerializer(serializers.ModelSerializer):

    customizationType = CustomizationTypeSerializer(allow_null=True)
    dimensions = DimensionSerializer(source = "commodity_dimensions",many=True)
    mediaCollection  = MediaCollectionSerializer(required=False)

    def create(self, validated_data):
        customization_data = validated_data.pop('customizationType')
        customization = CustomizationType.objects.create(**customization_data) if customization_data else None

        mediaCollection_data = validated_data.pop('mediaCollection')
        media = mediaCollection_data.pop('media')
        mediaCollection = MediaCollection.objects.create(**mediaCollection_data)
        mediaCollection.media.set(media)
        
        dimension_data = validated_data.pop('commodity_dimensions')
        
        commodity = Commodity.objects.create(mediaCollection = mediaCollection,customizationType = customization ,**validated_data)
        
        for dimension in dimension_data:
            Dimension.objects.create(commodity=commodity,**dimension)

        return commodity
    
    def update(self, instance, validated_data):

        customization_data = validated_data.pop('customizationType')
        dimension_data = validated_data.pop('commodity_dimensions')
        mediaCollection_data = validated_data.pop('mediaCollection')

        for item in validated_data:
            if Product._meta.get_field(item):
                setattr(instance, item, validated_data[item])
            
        customizationObj = instance.customizationType
        
        if customizationObj :
            for item in customization_data:
                if CustomizationType._meta.get_field(item):
                    setattr(customizationObj, item, customization_data[item])
            customizationObj.save()

        instance.mediaCollection.delete()
        media = mediaCollection_data.pop('media')
        mediaCollection = MediaCollection.objects.create(**mediaCollection_data)
        mediaCollection.media.set(media)
        instance.mediaCollection = mediaCollection
                
        instance.save()

        instance.product_dimensions.all().delete()

        for dimension in dimension_data:
            Dimension.objects.create(commodity=instance,**dimension)
        
        return instance

    class Meta:
        model=Commodity
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):

    customizationType = CustomizationTypeSerializer(allow_null=True,required=False)
    dimensions = DimensionSerializer(source = "product_dimensions",many=True,required=False,allow_null=True)
    mediaCollection  = MediaCollectionSerializer(required=False,allow_null=True)
    commodity = serializers.PrimaryKeyRelatedField(queryset = Commodity.objects.all(),required=False,allow_null=True)

    def create(self, validated_data):

        customization_data = validated_data.pop('customizationType')
        customization = CustomizationType.objects.create(**customization_data) if customization_data else None

        commodity = validated_data.pop('commodity',None)
        mediaCollection_data = validated_data.pop('mediaCollection',None)
        
        if mediaCollection_data:
            media = mediaCollection_data.pop('media',None)
            mediaCollection = MediaCollection.objects.create(**mediaCollection_data)
            mediaCollection.media.set(media)
        else:
            mediaCollection = None
        
        dimension_data = validated_data.pop('product_dimensions',None)
        product = Product.objects.create(mediaCollection = mediaCollection,commodity=commodity,customizationType = customization ,**validated_data)
        
        for dimension in (dimension_data or []):
            Dimension.objects.create(product=product,**dimension)

        return product
    
    def update(self, instance, validated_data):

        customization_data = validated_data.pop('customizationType',None)
        dimension_data = validated_data.pop('product_dimensions',None)
        commodity = validated_data.pop('commodity',None)
        mediaCollection_data = validated_data.pop('mediaCollection',None)
        
        for item in validated_data:
            if Product._meta.get_field(item):
                setattr(instance, item, validated_data[item])
            
        customizationObj = instance.customizationType
        
        if customizationObj :
            for item in customization_data:
                if CustomizationType._meta.get_field(item):
                    setattr(customizationObj, item, customization_data[item])
            customizationObj.save()

        if instance.mediaCollection:
            instance.mediaCollection.delete() 

        if mediaCollection_data:
            media = mediaCollection_data.pop('media',None)
            mediaCollection = MediaCollection.objects.create(**mediaCollection_data)
            mediaCollection.media.set(media)
            instance.mediaCollection = mediaCollection
        
        instance.commodity = commodity
        
        instance.save()
        if  instance.product_dimensions:
             instance.product_dimensions.all().delete()

        for dimension in (dimension_data or []):
            Dimension.objects.create(product=instance,**dimension)
        
        return instance
    class Meta:
        model=Product
        exclude = ['deleted_at']

class ProductListSerializer(serializers.ModelSerializer):
    customizationType = CustomizationTypeSerializer(required=False)
    dimensions = DimensionSerializer(source = "product_dimensions",many=True)
    mediaCollection = MediaCollectionListSerializer(required=False)
    commodity = serializers.PrimaryKeyRelatedField(queryset = Commodity.objects.all(),required=False)
    class Meta:
        model=Product
        fields='__all__'
