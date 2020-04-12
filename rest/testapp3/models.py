from django.db import models
import uuid

# Create your models here.
class Content(models.Model):
    content_id     =   models.UUIDField(primary_key=True,   default=uuid.uuid4, editable=False)
    content_slug   =   models.CharField(max_length=100,unique=True)
    content_title  =   models.CharField(max_length=100)
    content_subtitle   =   models.CharField(max_length=255,null=True, blank=True)
    content_headline   =   models.CharField(max_length=100)
    content_modifieddate   = models.DateField()
    content_createddate    = models.DateField()
     
    def __str__(self): # __unicode__ on Python 2
        return self.content_title

# Video model inhertis Content Model. 
class Video(Content):
    video_id    = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video_link  = models.URLField(null=True, blank=True)
    video_source_guid = models.CharField(max_length=255,null=True, blank=True)
    video_embed       = models.TextField(null=True, blank=True)
    video_copyright    = models.TextField(null=True, blank=True)
    
    def __str__(self): # __unicode__ on Python 2
         return self.content_title
