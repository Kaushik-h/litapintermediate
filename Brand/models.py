from django.db import models
import uuid
from litap.paranoid_model import ParanoidModel

class Brand(ParanoidModel):
    CATEGORY_TYPE_CHOICES = [
        ('Sports Shop','Sports Shop'),
        ('Car','Car'),
        ('Energy Drinks','Energy Drinks'),
        ('Clothing','Clothing')
    ]
    brandId = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True)
    name = models.CharField(max_length=40)
    category = models.CharField(choices=CATEGORY_TYPE_CHOICES,max_length=50)
    websiteLink = models.CharField(max_length=100,blank=True,null=True,default=None)
    logoCollections = models.ForeignKey('MediaCollection.MediaCollection',blank=True,null=True,default=None,on_delete=models.SET_NULL,related_name="brand_logo",db_constraint=False)
    advertisementCollections = models.ForeignKey('MediaCollection.MediaCollection',blank=True,null=True,default=None,on_delete=models.SET_NULL,related_name="brand_advertisement",db_constraint=False)
    def __str__(self):
        return f'{self.name}'