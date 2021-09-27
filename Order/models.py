from django.db import models
import uuid


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
       ('Processing','Processing'), 
        ('Shipped','Shipped'),
        ('Delivered','Delivered'),
        ('RefundInitiated','RefundInitiated'),
        ('RefundComplete','RefundComplete')
    ]
    
    orderId = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True)
    owner = models.ForeignKey('Auth.User',on_delete=models.CASCADE,related_name="orders")
    orderDate = models.DateTimeField(auto_now_add=True)
    deliveryDate = models.DateTimeField()
    deliveryAddress = models.ForeignKey('Location.PhysicalLocation',on_delete=models.PROTECT,null=True,default=None,blank=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    orderStatus = models.CharField(max_length=20,choices=ORDER_STATUS_CHOICES,default="Processing")
    orderProducts = models.ManyToManyField('Product.Product', through='OrderProducts',related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderProducts(models.Model):

    DELIVERY_TYPE_CHOICES = [
        ('Express','Express'),
        ('OneDay','OneDay'),
        ('Priority','Priority'),

    ]
    ORDER_STATUS_CHOICES = [
        ('Processing','Processing'), 
        ('Shipped','Shipped'),
        ('Delivered','Delivered'),
        ('RefundInitiated','RefundInitiated'),
        ('RefundComplete','RefundComplete')
    ]
    orderProductId = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True)
    product = models.ForeignKey('Product.Product',on_delete=models.CASCADE,related_name="orderObjects")
    order = models.ForeignKey('Order.Order',on_delete=models.CASCADE,blank=True,related_name="productObjects")
    dimension = models.ForeignKey('Product.Dimension',on_delete=models.CASCADE,blank=True,null=True)
    firstLocation = models.ForeignKey('Location.PhysicalLocation',on_delete = models.SET_NULL,null=True,blank=True,default=None)
    deliveryType = models.CharField(max_length=20,choices=DELIVERY_TYPE_CHOICES)
    isDelivered = models.BooleanField(default=False)
    deliveryDate = models.DateTimeField(null=True,blank=True,default=None)
    orderStatus = models.CharField(max_length=20,choices=ORDER_STATUS_CHOICES,default="Processing")
    giftReason = models.TextField(null=True,blank=True,default=None)
    GiftBioId = models.OneToOneField('Profile.Bio',null=True,blank=True,default=None,on_delete=models.SET_NULL)
class CartProducts(models.Model):
    cartProductId = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True)
    product = models.ForeignKey('Product.Product',on_delete=models.CASCADE,related_name="CartProductObjects")
    cart = models.ForeignKey('Order.Cart',on_delete=models.CASCADE,blank=True,related_name="CartObjects")
    dimension = models.ForeignKey('Product.Dimension',on_delete=models.CASCADE,blank=True,null=True)
    quantity = models.PositiveIntegerField(default=1)
    
    @property
    def cost(self):
        cost = 2
        return cost
class Cart(models.Model):
    cartId = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True)
    owner = models.OneToOneField('Auth.User',on_delete=models.CASCADE,related_name="cart")
    products = models.ManyToManyField('Product.Product',through='CartProducts',related_name='carts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    @property
    def cost(self):
        cost = 5
        return cost