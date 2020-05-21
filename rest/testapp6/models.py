from django.db import models
from datetimeutc.fields import DateTimeUTCField

# Create your models here.

class create_question(models.Model):

    L ='low'
    H ='high'
    M ='medium'

    _TYPES=(
        (L,'Low'),
        (H,'High'),
        (M,'Medium')
    )

    #question_mark               = models.IntegerField()
    #complexity                  = models.IntegerField()
    ques_type                   = models.CharField(max_length=100)
    importance                  = models.IntegerField(default=0)
    created_at                  = models.DateField(auto_now_add=True)
    updated_at                  = models.DateTimeField(auto_now=True)
    active                      = models.BooleanField(default=True,null=True,blank=True)

    def __str__(self):
        return str(self.ques_type)

class create_question_history(models.Model):

    L ='low'
    H ='high'
    M ='medium'

    _TYPES=(
        (L,'Low'),
        (H,'High'),
        (M,'Medium')
    )

    #question_mark               = models.IntegerField()
    #complexity                  = models.IntegerField()
    ques_type                   = models.CharField(max_length=100)
    importance                  = models.IntegerField(default=0)
    created_at                  = models.DateTimeField()
    updated_at                  = models.DateTimeField(auto_now=True)
    submitted                   = DateTimeUTCField(auto_now_add=True)
    active                      = models.BooleanField(default=True,null=True,blank=True)

    def __str__(self):
        return str(self.ques_type)
