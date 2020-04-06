from django.db import models

class add_subject(models.Model):

    subject_name        = models.CharField(max_length=150)
    subject_description = models.CharField(max_length=250,null=True,blank=True)

    def __str__(self):
        return self.subject_name

class create_super_book(models.Model):
    title            = models.CharField('Title', null=True, blank=True, max_length=255)
    my_order         = models.PositiveIntegerField(default=0, blank=False, null=False)
    subject_name     = models.ForeignKey(add_subject,related_name="subject_list",blank=True,on_delete="DO_NOTHING")

    class Meta(object):
        ordering = ['my_order']

class Button(models.Model):
    """A button"""
    name = models.CharField(max_length=64)
    button_text = models.CharField(max_length=64)

class Panel(models.Model):
    """A Panel of Buttons - this represents a control panel."""
    name = models.CharField(max_length=64)
    buttons = models.ManyToManyField(Button, through='PanelButtons')

class PanelButtons(models.Model):
    """This is a junction table model that also stores the button order for a panel."""
    panel = models.ForeignKey(Panel,on_delete="DO_NOTHING")
    button = models.ForeignKey(Button,on_delete="DO_NOTHING")
    button_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('button_order',)
