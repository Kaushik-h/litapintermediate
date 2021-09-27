
from django.db import models
from Auth.models import User
import uuid

class Event(models.Model):  
    EVENT_TYPE_CHOICES = [
            ('online','online'), 
            ('offline','offline'),
            ('public','public'),
            ('private','private')
        ]

    eventId = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True)
    name = models.CharField(max_length=40)
    organizer = models.ForeignKey('Auth.User',on_delete=models.PROTECT)
    participants =  models.ManyToManyField('Auth.User',blank=True,related_name="events")
    eventType = models.CharField(choices=EVENT_TYPE_CHOICES,max_length=40)
    eventDescription = models.TextField()
    eventPasscode = models.CharField(max_length=40,null=True,default=None,blank=True)
    location = models.ForeignKey('Location.PhysicalLocation',db_constraint=False,on_delete=models.SET_NULL,null=True,default=None,blank=True,db_column="location")
    eventUrl = models.URLField(max_length=500,null=True,default=None,blank=True)
    mediaCollection = models.ForeignKey('MediaCollection.MediaCollection',db_constraint=False,blank=True,default=None,null=True,on_delete=models.SET_NULL,db_column ="mediaCollection")
    maxParticipants = models.PositiveIntegerField(null=True,default=None,blank=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2,null=True,blank=True,default=True)
    eventTimeStamp = models.DateTimeField(null=True,default=None,blank=True)
    eventDate = models.DateField(null=True,default=None,blank=True)
    eventTime = models.TimeField(null=True,default=None,blank=True)
    eventDuration = models.DurationField(null=True,default=None,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.organizer.username} - {self.name}' 