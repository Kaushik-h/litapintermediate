from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q
from django.conf import settings
from django.utils.crypto import get_random_string
import uuid
# Create your models here.

def RandomKeyGenerator():
    return get_random_string(length=128)


class User(AbstractUser):
    userId = models.CharField(max_length=250,primary_key=True,default=uuid.uuid4,editable=False)
    username = models.CharField(max_length=12,unique = True)
    firstName = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20,null=True,default=None)
    lastName = models.CharField(max_length=20)
    isTribeLeader = models.BooleanField(blank=True,null=True,default=False)
    isModerator = models.BooleanField(blank=True,null=True,default=False)
    kyc = models.OneToOneField('Profile.KYC',on_delete=models.PROTECT,null=True,blank=True,default=None)
    primaryPhone = models.CharField(max_length=20,null=True,blank=True,default=None,unique=True)
    primaryEmail = models.EmailField(null=True,blank=True,default=None,unique=True)
    followers = models.ManyToManyField('User',related_name="followee",blank=True)
    
    primaryPhoneVerified = models.BooleanField(null=True,blank=True,default=False)
    primaryEmailVerified = models.BooleanField(null=True,blank=True,default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["primaryEmail"]

    
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=(
                        ~Q(
                            Q(primaryPhone__isnull=True) & Q(primaryEmail__isnull=True)
                            ) 
            ),name='primaryEmail_primaryPhone_not_both_null')
    ]

class CallbackToken(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name=None, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    key = models.CharField(default=RandomKeyGenerator, max_length=128, unique=True)