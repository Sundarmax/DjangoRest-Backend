from django.db import models
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    published = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100)
    tags = TaggableManager()

    def __str__(self):
        return self.title


class Website(models.Model):
  url = models.URLField(unique=True)

class Page(models.Model):
  website = models.ForeignKey(
    'Website',
    on_delete=models.CASCADE,
    related_name='pages'
  )
  url = models.URLField(max_length=2083)
  title = models.CharField(max_length=255)
  content = models.TextField()