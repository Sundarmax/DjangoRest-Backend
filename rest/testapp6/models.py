from django.db import models

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

    question_mark               = models.IntegerField()
    importance                  = models.IntegerField()
    complexity                  = models.IntegerField()
    active                      = models.BooleanField(default=True,null=True,blank=True)

    def __str__(self):
        return str(self.question_mark)
