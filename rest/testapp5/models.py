from django.db import models
from django.contrib.postgres.fields import JSONField

class skill_category(models.Model):

    skill_category_name   = models.CharField(max_length=155)
    description           = models.CharField(max_length=255,blank=True,null=True)
    active                = models.BooleanField(default=True,null=True,blank=True)

    def __str__(self):
        return self.skill_category_name

    class Meta:
        db_table = 'skill_category'

class skill_book_name(models.Model):

    skill_book_name =   models.CharField(max_length=155)
    description     =   models.CharField(max_length=255,blank=True,null=True)
    skill_category  =   models.ForeignKey(skill_category,related_name="skill_categories", on_delete=models.CASCADE )
    skill_topics_order = JSONField(null=True,blank=True)
    active          =   models.BooleanField(default=True,null=True,blank=True)

    def __str__(self):
        return self.skill_book_name
    
    class Meta:
        db_table = 'skill_book_name'

class skill_topic(models.Model):

    skill_topic_name =   models.CharField(max_length=155)
    description     =   models.CharField(max_length=255,blank=True,null=True)
    skill_book      =   models.ForeignKey(skill_book_name,related_name="skill_book_names", on_delete=models.CASCADE )
    skills_order    =   JSONField(null=True,blank=True)
    active          =   models.BooleanField(default=True,null=True,blank=True)

    def __str__(self):
        return self.skill_topic_name
    
    class Meta:
        db_table = 'skill_topic'

class skill(models.Model):

    skill_name      =   models.CharField(max_length=155)
    description     =   models.CharField(max_length=255,blank=True,null=True)
    skill_topic     =   models.ForeignKey(skill_topic,related_name="skill_topics", on_delete=models.CASCADE )
    active          =   models.BooleanField(default=True,null=True,blank=True)

    def __str__(self):
        return self.skill_name
    
    class Meta:
        db_table = 'skill'

""" class skills_successor(models.Model):
    skill           =   models.ForeignKey(skill,null=True,related_name='parent_skill',on_delete=models.CASCADE )
    skill_successor =   models.ForeignKey(skill,null=True,related_name='next_skill',on_delete=models.CASCADE )
    weightage       =   models.IntegerField(null=True,blank=True)

    class Meta:
        db_table = 'skills_successor'

 """
