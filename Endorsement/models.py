from django.db import models


class Endorsement(models.Model):
    endorsementdId = models.AutoField(primary_key=True)
    brand = models.ForeignKey('Brand.Brand',on_delete=models.CASCADE,db_constraint=False)
    commodities = models.ManyToManyField('Product.Commodity',related_name="endorsements")
    user = models.ForeignKey('Auth.User',on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    terms = models.TextField()
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2,null=True,default=None,blank=True)
    advertisementCollections = models.OneToOneField('MediaCollection.MediaCollection',null=True,blank=True,default=None,on_delete=models.SET_NULL,db_constraint=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class EndorsementRequest(models.Model):
    ENDORSEMENT_STATUS_CHOICES = [
            ('InProgress','InProgress'), 
            ('PendingDocumentVerification','PendingDocumentVerification'),
            ('PendingIdentityVerification','PendingIdentityVerification'),
            ('Approved','Approved'),
            ('Rejected','Rejected')]
    user = models.OneToOneField('Auth.User',on_delete=models.CASCADE,related_name="endorsement_request",null=True)
    endorsement = models.ForeignKey('Endorsement.Endorsement',on_delete=models.CASCADE,related_name="requests",null=True)
    judgedBy = models.ForeignKey('Auth.User',null=True,blank=True,default=None,on_delete = models.SET_NULL)
    # requestTime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=ENDORSEMENT_STATUS_CHOICES,max_length=60)
    collection = models.OneToOneField('MediaCollection.MediaCollection',null=True,blank=True,default=None,on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
