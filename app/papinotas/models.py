from __future__ import unicode_literals

from django.db import models

# Create your models here. 


class Groups(models.Model):
    name = models.CharField(max_length=40)
    group_type = models.IntegerField(null=True, blank=True)
    group_section = models.CharField(max_length=40)
    student_counter = models.IntegerField(null=True, blank=True)
    has_changes = models.BooleanField(default=False)
    
    def __unicode__(self):
        return u"%s" % self.name


class Students(models.Model):
    name = models.CharField(max_length=40)
    self = models.BooleanField(default=False)
    ap1 = models.BooleanField(default=False)
    ap2 = models.BooleanField(default=False)
    groups = models.ForeignKey(Groups, null = True, blank = True)

    def __unicode__(self):
        return u"%s" % self.name
   
        