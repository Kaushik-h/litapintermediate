from django.db import models
from django.core.validators import FileExtensionValidator
from MediaCollection.models import MediaCollection
import uuid

# Create your models here.
class Media(models.Model):

    MEDIA_TYPE_CHOICES = [
            ('Audio','Audio'), 
            ('Video','Video'),
            ('Image','Image'),
            ('Document','Document')
        ]
    mediaId = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True)
    name = models.CharField(max_length=40)
    mediaType = models.CharField(max_length=20,choices=MEDIA_TYPE_CHOICES)
    value = models.FileField(upload_to='media',validators=[FileExtensionValidator(['png', 'jpg', 'svg','jpeg','pdf'])])
    mediaCollection = models.ForeignKey('MediaCollection.MediaCollection',related_name='media',on_delete = models.SET_NULL,null=True,blank=True) 