from django.db import models
import uuid

class PhysicalLocation(models.Model):
    addressId = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True)
    addressLine1 = models.CharField(max_length=40)
    addressLine2 = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    zipcode = models.CharField(max_length=20)
    mailCode = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)