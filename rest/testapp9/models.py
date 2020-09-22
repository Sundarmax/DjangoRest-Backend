
from django.db import models

class Snippet(models.Model):
    
    title       = models.CharField(max_length=100, blank=True, default='')
    code        = models.TextField()
    created     = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


