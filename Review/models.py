from django.db import models
import uuid
from litap.utils import deleted_user
class Review(models.Model):

    reviewId = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True)
    name = models.CharField(max_length=40)
    writerUser = models.ForeignKey('Auth.User',related_name="reviews",on_delete=models.SET(deleted_user))
    product = models.ForeignKey('Product.Product',on_delete=models.CASCADE,null=True,blank=True,default=None)
    rating = models.CharField(max_length=5)
    mediaCollection = models.OneToOneField('MediaCollection.MediaCollection',null=True,blank=True,default=None,on_delete=models.SET_NULL)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)