from django.db import models




class BookManager(models.Manager):
    def title_count(self,keyword):
        return self.filter(title__icontains=keyword).count()


# Testing Model Managers 
class Book(models.Model):

    title = models.CharField(max_length = 100)
    price = models.IntegerField()

    objects = BookManager()

    def __str__(self):
        return self.title


