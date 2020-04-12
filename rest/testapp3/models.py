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

# Models which can be created for testing aggregation and annotation. 
class Department(models.Model):
    dept_name = models.CharField(max_length = 100)
    established_on = models.DateField()
    
    def __str__(self): # __unicode__ on Python 2
         return self.dept_name

class Level(models.Model):
    level_name = models.CharField(max_length = 100)
    pay_min = models.PositiveIntegerField()
    pay_max = models.PositiveIntegerField()

    def __str__(self): # __unicode__ on Python 2
         return self.level_name

class Employee(models.Model):
    emp_name = models.CharField(max_length = 100)
    department = models.ForeignKey(Department,on_delete ="DO_NOTHING")
    level = models.ForeignKey(Level,on_delete="DO_NOTHING")
    #reports_to = models.ForeignKey('self', null=True, blank=True)
    pay = models.PositiveIntegerField()
    joined_on = models.DateField()

class Leave(models.Model):
    employee = models.ForeignKey(Employee,on_delete = "DO_NOTHING")
    leave_day = models.DateField()

