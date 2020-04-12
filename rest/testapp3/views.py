from django.shortcuts import render
from .models import Video,Content
import uuid
import datetime

#Model inhertiance establish 1:1 Relationships b/w two models. 

def TestModelInheritance():
    test  =  uuid.uuid4() 
    TDate = datetime.date.today() 
    videoIns = Video()
    videoIns.video_id = test
    #Base class content Table
    videoIns.content_createddate = TDate
    videoIns.content_modifieddate= TDate
    videoIns.content_headline = "Rural Development"
    videoIns.content_title = "Industrial Evolution"
    videoIns.content_slug = "New Revolution"
    videoIns.save()
    print('Record inserted')

#TestModelInheritance()

