
from Order.models import *
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from rest_framework.permissions import  IsAuthenticated
from Product.serializers import ProductListSerializer,DimensionSerializer

class OrderProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderProducts
        fields='__all__'

class OrderProductsListSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()
    dimension = DimensionSerializer()
    class Meta:
        model=OrderProducts
        fields='__all__'

class OrderListSerializer(serializers.ModelSerializer):
    orderProducts = OrderProductsListSerializer(many=True,source = "productObjects")
    class Meta:
        model=Order
        fields= '__all__'  

class OrderSerializer(serializers.ModelSerializer):

    orderProducts = OrderProductsSerializer(many=True,source = "productObjects")
    
    def create(self, validated_data):
        products_data = validated_data.pop('productObjects')
        order = Order.objects.create(**validated_data)
        for product_data in products_data:
            OrderProducts.objects.create(order=order,**product_data)
        return order
    
    def update(self, instance, validated_data):
        products_data = validated_data.pop('productObjects')
        for item in validated_data:
            if Order._meta.get_field(item):
                setattr(instance, item, validated_data[item])
        OrderProducts.objects.filter(order=instance).delete()
        for product_data in products_data:
            OrderProducts.objects.create(order = instance,**product_data)
        instance.save()
        return instance
        
    class Meta:
        model=Order
        fields= '__all__'
class CartProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartProducts
        fields='__all__'

class CartProductsListSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    dimension = DimensionSerializer(read_only=True)
    class Meta:
        model=CartProducts
        fields='__all__'
class CartListSerializer(serializers.ModelSerializer):
    products = CartProductsListSerializer(many=True,source="CartObjects")
    class Meta:
        model=Cart
        fields= '__all__'

class CartSerializer(serializers.ModelSerializer):
    products = CartProductsSerializer(many=True,source="CartObjects")
    def update(self, instance, validated_data):
        cart_products_data = validated_data.pop('CartObjects')
        for item in validated_data:
            if Cart._meta.get_field(item):
                setattr(instance, item, validated_data[item])
        CartProducts.objects.filter(cart=instance).delete()
        for cart_product in cart_products_data:
            CartProducts.objects.create(cart = instance,**cart_product)
        instance.save()
        return instance
    class Meta:
        model=Cart
        fields= '__all__'