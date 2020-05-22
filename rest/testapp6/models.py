from django.db import models
from datetimeutc.fields import DateTimeUTCField

from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

class create_question(models.Model):

    L ='low'
    H ='high'
    M ='medium'

    _TYPES=(
        (L,'Low'),
        (H,'High'),
        (M,'Medium')
    )

    ques_type                   = models.CharField(max_length=100)
    importance                  = models.IntegerField(default=0)
    #current_version_id          = models.IntegerField(null=True,blank=True)
    created_at                  = DateTimeUTCField(auto_now_add=True)
    updated_at                  = DateTimeUTCField(auto_now=True)
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
    ques_type                   = models.CharField(max_length=100)
    question_id                 = models.ForeignKey(create_question,null=True,blank=True,on_delete="DO_NOTHING")
    importance                  = models.IntegerField(default=0)
    #version_id                  = models.IntegerField(null=True,blank=True)
    created_at                  = DateTimeUTCField(auto_now_add=True)
    updated_at                  = DateTimeUTCField(auto_now=True)
    active                      = models.BooleanField(default=True,null=True,blank=True)

    def __str__(self):
        return str(self.ques_type)


@receiver(post_save, sender=create_question)
def add_version_of_question(sender, instance, created, **kwargs):
    if created:
        _contentHistory = create_question_history()
        _contentHistory.ques_type = instance.ques_type
        _contentHistory.question_id = instance
        _contentHistory.importance  = instance.importance
        _contentHistory.created_at  = instance.created_at
        _contentHistory.updated_at  = instance.updated_at
        _contentHistory.save()
    else:
        # Get diff between two timestamp
        _incomingTimestamp = instance.updated_at
        # Get latest record from history table. 
        _CheckExist   = create_question_history.objects.filter(question_id= instance.id).exists()
        if _CheckExist:
            _latestRecord   = create_question_history.objects.filter(question_id= instance.id).last()
            _previousTimestamp = _latestRecord.updated_at
            diff = int(_incomingTimestamp.timestamp() - _previousTimestamp.timestamp())
            print(diff)
            if diff >120:
                _contentHistory = create_question_history()
                _contentHistory.ques_type = instance.ques_type
                _contentHistory.question_id = instance
                _contentHistory.importance  = instance.importance
                _contentHistory.created_at  = instance.created_at
                _contentHistory.updated_at  = instance.updated_at
                _contentHistory.save()
            else:
                _contentHistory = create_question_history.objects.get(id = _latestRecord.id)
                _contentHistory.ques_type   = instance.ques_type
                _contentHistory.question_id = instance
                _contentHistory.importance  = instance.importance
                _contentHistory.created_at  = instance.created_at
                _contentHistory.updated_at  = instance.updated_at
                _contentHistory.save()