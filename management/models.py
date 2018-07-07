from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import *
from django.conf import settings
# Create your models here.

class flat_info(models.Model):
    flat_no = models.IntegerField( null=False, primary_key=True)
    contact_no = models.IntegerField(null=False)
    owner_name = models.CharField(max_length=50, null=False)
    residence = models.CharField(max_length=50, null=False,)
    occupation = models.CharField(max_length=50, null=False,)
    email = models.CharField(max_length=100, null=False,)
    members = models.IntegerField( null=False)
    floor = models.IntegerField( null=False)

    def __unicode__(self):
        return '%s' % (self.flat_no)

class management(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_no = models.IntegerField(default='',null=True)
    address = models.CharField(default='',max_length=50, null=True)
    designation = models.CharField(default='',max_length=50, null=True)
    def __unicode__(self):
        return '%s' % (self.user)

class notice(models.Model):
    notice_sub = models.CharField(max_length=50, null=False)
    date_created=models.DateTimeField(auto_now=True,blank=True,null=True)
    notice_details = models.CharField(max_length=300, null=False)
    author=models.ForeignKey(management,blank=True,null=True)
    def __unicode__(self):
        return '%s' % (self.notice_sub)

class event(models.Model):
    event_sub = models.CharField(max_length=50, null=False)
    date_created=models.DateTimeField(auto_now=True,blank=True,null=True)
    event_details = models.CharField(max_length=300, null=False)
    author=models.ForeignKey(management,blank=True,null=True)
    def __unicode__(self):
        return '%s' % (self.event_sub)


class complaint(models.Model):
    email = models.CharField(max_length=100, null=False,)
    flat_no=models.IntegerField(blank=True,null=True)
    date_created=models.DateTimeField(auto_now=True,blank=True,null=True)
    complaint_sub = models.CharField(max_length=150, null=False)
    complaint_details = models.CharField(max_length=300, null=False)
    complaint_status = models.CharField(max_length=5, null=False, default="open")

    def __unicode__(self):
        return '%s' % (self.flat_no)


class maintenance_type(models.Model):
        maintenance_header = models.CharField(max_length=100, null=False, primary_key=True)
        amount = models.FloatField()
        counter = models.FloatField(blank=True, null=True)

        def __unicode__(self):
            return '%s' % (self.maintenance_header)

class fyi1(models.Model):
    financial_year=models.CharField(max_length=9, null=False, primary_key=True)
    maintenance_counter=models.FloatField(blank=True, null=True,default=0.0)
    parking_counter=models.FloatField(blank=True, null=True,default=0.0)
    sinkingfund_counter=models.FloatField(blank=True, null=True,default=0.0)
    def __unicode__(self):
        return '%s' % (self.financial_year)

class maintenance(models.Model):
    flat_no = models.CharField( blank=True, null=True,max_length=4)
    date_time = models.DateTimeField(blank=True, null=True, auto_now=True)
    financial_year=models.ForeignKey(fyi1)
    maintenance_counter=models.FloatField(blank=True, null=True,default=0.0)
    parking_counter=models.FloatField(blank=True, null=True,default=0.0)
    sinkingfund_counter=models.FloatField(blank=True, null=True,default=0.0)
    type_of_maintenance = models.ForeignKey(maintenance_type)
    amount = models.FloatField(blank=True, null=True,default=0.0)
    fine = models.FloatField(blank=True, null=True,default=0.0)
    total_amount=models.FloatField(blank=True, null=True,default=0.0)
    def __unicode__(self):
        return '%s' % (self.flat_no)

class contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=100)
    query = models.TextField(max_length=300, null=False)
    def __unicode__(self):
        return '%s' % (self.name)

class tid(models.Model):
    flat_no=models.IntegerField(null=False, primary_key=True)
    maintenance_count=models.FloatField(blank=True, null=True,default=0.0)
    parking_count=models.FloatField(blank=True, null=True,default=0.0)
    sinkingfund_count=models.FloatField(blank=True, null=True,default=0.0)
    last_id = models.IntegerField(blank=True, null=True,default=0)
    sinkingfund_paid=models.FloatField(blank=True, null=True,default=0.0)
    sinkingfund_fine_paid=models.FloatField(blank=True, null=True,default=0.0)
    parking_paid=models.FloatField(blank=True, null=True,default=0.0)
    parking_fine_paid=models.FloatField(blank=True, null=True,default=0.0)
    maintenance_paid=models.FloatField(blank=True, null=True,default=0.0)
    maintenance_fine_paid=models.FloatField(blank=True, null=True,default=0.0)
    def __unicode__(self):
        return '%s' % (self.flat_no)
