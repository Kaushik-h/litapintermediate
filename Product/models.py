from django.db import models
from django.db.models import Q
from litap.paranoid_model import ParanoidModel
import uuid

class Product(ParanoidModel):

    PRODUCT_TYPE_CHOICES = [
            ('Ball','Ball'), 
            ('Bat','Bat'),
            ('Guards','Guards'),
            ('Studs','Studs'),
            ('Jersey','Jersey'),
            ('Shorts','Shorts'),
            ('Cap','Cap'),
            ('Image','Image')
        ]
    
    productId = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True)
    name = models.CharField(max_length=40)
    owner = models.ForeignKey('Auth.User',on_delete=models.CASCADE)
    productType = models.CharField(max_length=20,choices=PRODUCT_TYPE_CHOICES)
    mediaCollection = models.OneToOneField('MediaCollection.MediaCollection',null=True,blank=True,default=None,on_delete=models.SET_NULL)
    description = models.TextField()
    rating = models.CharField(max_length=5,null=True,blank=True,default=None)
    isDisabled = models.BooleanField(default=False)
    # cost = models.DecimalField(max_digits=6, decimal_places=2)
    brand = models.ForeignKey('Brand.Brand',related_name="products",null=True,blank=True,default=None,on_delete=models.CASCADE)
    customizationType = models.OneToOneField('Product.CustomizationType',on_delete=models.SET_NULL,null=True,default=None,blank=True,related_name="product_customization")
    commodity = models.ForeignKey('Product.Commodity',on_delete=models.SET_NULL,null=True,default=None,blank=True,related_name="product")
    def __str__(self):
        return f'{self.name}'

class CustomizationType(models.Model):
    CUSTOMIZATION_TYPE_CHOICES = [
        ('Signature','Signature'),
        ('Message','Message')
    ]
    customizationTypeId = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20,choices=CUSTOMIZATION_TYPE_CHOICES)
    value = models.CharField(max_length=100,null=True,blank=True,default=None)
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=( 
                        (Q(type__exact='Signature') & Q(value__isnull=True))
                        |
                        (Q(type__exact='Message') & Q(value__isnull=False))  
                    )    
            ,name='customization_type_signature_must_be_null_value'),
    ]

class Commodity(ParanoidModel):
    PRODUCT_TYPE_CHOICES = [
            ('Ball','Ball'), 
            ('Bat','Bat'),
            ('Guards','Guards'),
            ('Studs','Studs'),
            ('Jersey','Jersey'),
            ('Shorts','Shorts'),
            ('Cap','Cap'),
            ('Image','Image')
        ]
    
    commodityId = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True)
    name = models.CharField(max_length=40)
    owner = models.ForeignKey('Auth.User',on_delete=models.CASCADE)
    commodityType = models.CharField(max_length=20,choices=PRODUCT_TYPE_CHOICES)
    mediaCollection = models.OneToOneField('MediaCollection.MediaCollection',null=True,blank=True,default=None,on_delete=models.SET_NULL,db_constraint=False)
    description = models.TextField()
    rating = models.CharField(max_length=5,null=True,blank=True,default=None)
    isDisabled = models.BooleanField(default=False)
    # cost = models.DecimalField(max_digits=6, decimal_places=2)
    brand = models.ForeignKey('Brand.Brand',related_name="commodities",null=True,blank=True,default=None,on_delete=models.CASCADE)
    customizationType = models.OneToOneField('Product.CustomizationType',on_delete=models.SET_NULL,null=True,default=None,blank=True,related_name="commodity_customization")
    
    def __str__(self):
        return f'{self.name}'
    
class Dimension(models.Model):
    SIZE_CHOICES = [
            ('XS','XS'),('S','S'),('M','M'),
            ('L','L'),('XL','XL'),('XXL','XXL'),
            ('5','5'),('6','6'),('7','7'),
            ('8','8'),('9','9'),('10','10'),('11','11')]
    dimensionId = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True)
    product = models.ForeignKey('Product.Product',related_name="product_dimensions",null=True,blank=True,default=None,on_delete=models.CASCADE)
    commodity = models.ForeignKey('Product.Commodity',related_name="commodity_dimensions",null=True,blank=True,default=None,on_delete=models.CASCADE)
    size = models.CharField(max_length=10,choices=SIZE_CHOICES,null=True,blank=True,default=None)
    color = models.CharField(max_length=20,null=True,blank=True,default=None)
    count = models.IntegerField(null=True,blank=True,default=None)
    length = models.IntegerField(null=True,blank=True,default=None)
    width = models.IntegerField(null=True,blank=True,default=None)
    height = models.IntegerField(null=True,blank=True,default=None)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    lastUpdatedOrder = models.DateTimeField(null=True,blank=True,default=None)
    lastUpdatedUser = models.DateTimeField(null=True,blank=True,default=None)
    lastUpdatedTime = models.DateTimeField(null=True,blank=True,default=None)
