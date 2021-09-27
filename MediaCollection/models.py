from django.db import models
import uuid

class MediaCollection(models.Model):
    COLLECTION_TYPE_CHOICES = [
            ('ProductMediaCollection','ProductMediaCollection'), 
            ('LogoCollection','LogoCollection'),
            ('ReviewMediaCollection','ReviewMediaCollection'),
            ('BrandMediaCollection','BrandMediaCollection'),
            ('EventMediaCollection','EventMediaCollection')
        ]
    COLLECTION_SEVERITY_CHOICES = [
            ('Confidential','Confidential'), 
            ('Public','Public'),
            ('Private','Private')
        ]
    collectionId =  models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True)
    collectionType = models.CharField(max_length=30,choices=COLLECTION_TYPE_CHOICES)
    collectionSeverity = models.CharField(max_length=30,choices=COLLECTION_SEVERITY_CHOICES)
