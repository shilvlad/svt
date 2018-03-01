# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class SvtType(models.Model):
    pass

class SvtUnit(models.Model):
    year_of_service = models.CharField(max_length=4, editable = True)
    month_of_service = models.CharField(max_length=2, editable=True)
    bar_code = models.CharField(max_length=10, editable=True)
    type = models.CharField(max_length=100, editable=True)
    sn = models.CharField(max_length=50, editable=True)
    desc = models.CharField(max_length=100, editable=True)
    def __unicode__(self):
        return str(self.bar_code)

class SvtPeriod(models.Model):
    year_of_service = models.CharField(max_length=4, editable=True)
    month_of_service = models.CharField(max_length=2, editable=True)
    upload = models.FileField(upload_to=u'uploads')
    def __unicode__(self):
        return str(self.year_of_service) + str(self.month_of_service)