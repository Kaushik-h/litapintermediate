from django.db import models
import uuid

# Create your models here.
class KYC(models.Model):

        KYC_STATUS_CHOICES = [
            ('NotStarted','NotStarted'), 
            ('Incomplete','Incomplete'),
            ('CompeletedSuccessful','CompeletedSuccessful'),
            ('Expired','Expired')
        ]
        KYC_IDENTIFICATION_TYPE_CHOICES = [
            ('Passport','Passport'), 
            ('NationalId','NationalId'),
            ('License','License') 
        ]
        KYC_VERIFICATION_TYPE_CHOICES = [
            ('BANK','BANK'), 
            ('LITAP','LITAP')
        ]
        
        kycId = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True)
        kycStatus = models.CharField(choices=KYC_STATUS_CHOICES,max_length=20)
        kycDate = models.DateTimeField()
        country = models.CharField(max_length=20)
        identityId = models.CharField(max_length=20,null=True,blank=True,default=None)
        identityType = models.CharField(max_length=20,choices=KYC_IDENTIFICATION_TYPE_CHOICES,null=True,blank=True,default=None)
        verificationType = models.CharField(max_length=20,choices=KYC_VERIFICATION_TYPE_CHOICES)

class Tribe(models.Model):

    tribeId = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True)
    tribeLeader = models.ForeignKey('Auth.User',on_delete=models.CASCADE)
    fans = models.ManyToManyField('Auth.User',related_name="tribes",blank=True)
    bio = models.TextField()
    tribeDescription = models.TextField()
    moderator = models.ForeignKey('Auth.User',related_name="tribeModerator",on_delete = models.SET_NULL,null=True,blank=True)

class Bio(models.Model):

    bioId = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True)
    user = models.OneToOneField('Auth.User',on_delete=models.CASCADE,related_name="bio")
    age = models.PositiveIntegerField()
    interests = models.CharField(max_length=100)
    clubs = models.CharField(max_length=100)
    records = models.CharField(max_length=100)
    mediaCollection = models.OneToOneField('MediaCollection.MediaCollection',null=True,blank=True,default=None,on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class LeaderRequest(models.Model):
    REQUEST_STATUS_CHOICES = [
            ('InProgress','InProgress'), 
            ('PendingDocumentVerification','PendingDocumentVerification'),
            ('PendingIdentityVerification','PendingIdentityVerification'),
            ('Approved','Approved'),
            ('Rejected','Rejected')]
    user = models.OneToOneField('Auth.User',on_delete=models.CASCADE,related_name="leader_request")
    approvedBy = models.ForeignKey('Auth.User',null=True,blank=True,default=None,on_delete = models.SET_NULL)
    # requestTime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=REQUEST_STATUS_CHOICES,max_length=60)
    collectionId = models.OneToOneField('MediaCollection.MediaCollection',null=True,blank=True,default=None,on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
