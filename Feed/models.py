from django.db import models
import uuid

# Create your models here.
class Feed(models.Model):

    CONTENT_TYPE_CHOICES = [
            ('Audio','Audio'), 
            ('Video','Video'),
            ('Text','Text'),
            ('Mix','Mix')
        ]

    feedId = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True)
    writer = models.ForeignKey('Auth.User',on_delete=models.PROTECT)
    createTime = models.DateTimeField()
    likes = models.PositiveIntegerField(default = 0)
    description = models.TextField(null=True,blank=True,default=None)
    contentType = models.CharField(max_length=20,choices=CONTENT_TYPE_CHOICES)
    mediaCollection = models.OneToOneField('MediaCollection.MediaCollection',on_delete=models.PROTECT,related_name="feed",null=True,blank=True,default=None)
    public = models.BooleanField()
    shareOption = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)