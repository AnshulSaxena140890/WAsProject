# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.

class Task(models.Model):
    taskID = models.AutoField(primary_key=True)
    taskName = models.CharField(max_length=200)
    taskBrief = models.TextField()
    isDone = models.BooleanField(default=False)
    createdAt = models.DateTimeField(default=timezone.now)
    doneAt = models.DateTimeField(blank=True,null=True)

    def Done(self):
        self.doneAt=timezone.now()
        self.isDone = True
        self.save()

    def __str__(self):
        return self.taskName

    def get_absolute_url(self):
        return reverse("task_list")
