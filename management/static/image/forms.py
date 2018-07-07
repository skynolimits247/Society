from __future__ import unicode_literals
from django.test import TestCase
from django import forms
from .models import *
from .views import *
from django.db import models
from django.contrib.auth.models import User
from .models import flat_info
from django.contrib.auth.models import AbstractUser
from resident.models import *


class conform(forms.ModelForm):
    email=forms.CharField(widget=forms.EmailInput
                          (attrs={'class':'panel','length':'100'}),
                          label="Enter your Email",
                          max_length=80,
                          required=True)
    name=forms.CharField(widget=forms.TextInput
                             (attrs={'class':'panel','length':'100'}),
                             label="Enter you Name",
                             max_length=80,
                             required=True)
    def clean_email(self):
        umail=self.cleaned_data['email']
        try:
            match=contact.objects.get(email=umail)
            print "match=",match
        except:
            return self.cleaned_data['email']
        raise forms.ValidationError('email already registered..!!')
    class Meta:
        model=contact
        fields=['email','name']

class dir1(forms.ModelForm):
    class Meta:
        model=flat_info
        fields= ['flat_no','owner_name','contact_no','occupation','email']

class resihomeform(forms.ModelForm):
    complaint_sub=forms.CharField(widget=forms.TextInput
                          (attrs={'class':'form-control'}),
                          label="Enter complaint subject",
                          required=True)
    complaint_details=forms.CharField(widget=forms.TextInput
                             (attrs={'class':'form-control'}),
                             label="Enter complaint details",
                             max_length=30,
                             required=True)
    class Meta:
        model=complaint
        fields=['flat_no','complaint_sub','complaint_details','complaint_status']

class noticeform(forms.ModelForm):
    notice_sub=forms.CharField(widget=forms.TextInput
                          (attrs={'class':'form-control'}),
                          label="Enter complaint subject",
                          required=True)
    notice_details=forms.CharField(widget=forms.TextInput
                             (attrs={'class':'form-control'}),
                             label="Enter complaint details",
                             max_length=30,
                             required=True)
    class Meta:
        model=complaint
        fields=['notice_sub','notice_details','complaint_status']

class Editownerforms(forms.ModelForm):
    email=forms.EmailField(widget=forms.TextInput
                          (attrs={'class':'form-control','readonly':'True'}),
                          label="Enter your Email",
                          required=True,)
    password=forms.CharField(widget=forms.PasswordInput
                             (attrs={'class':'form-control'}),
                             label="Type your password",
                             max_length=30,
                             required=True)
    confirm_password=forms.CharField(widget=forms.PasswordInput
                             (attrs={'class':'form-control'}),
                            label="Confirm your password",
                             max_length=30,
                             required=True)

    def clean_confirm_password(self):
        print"pass check"
        print "i= pass_",self.cleaned_data
        pas=self.cleaned_data['password']
        conpass=self.cleaned_data['confirm_password']
        print "i= conpass_",self.cleaned_data['confirm_password']
        print"pass=",pas,"conpass=",conpass
        if pas != conpass:
            raise forms.ValidationError('password and confirm password do not match...!')
        else:
            return self.cleaned_data['password']
    class Meta:
        model=management
        fields=['email','password']

class Editflatinfoforms(forms.ModelForm):
        contact_no=forms.CharField(widget=forms.TextInput
                                     (attrs={'class':'form-control'}),
                                     label="Enter your Contact Number",
                                     required=True)
        occupation=forms.CharField(widget=forms.TextInput
                                     (attrs={'class':'form-control'}),
                                     label="Enter your Occupation",
                                     required=True)
        members=forms.CharField(widget=forms.TextInput
                                     (attrs={'class':'form-control'}),
                                     label="Enter the number of family members",
                                     required=True)
        residence=forms.CharField(widget=forms.TextInput
                                     (attrs={'class':'form-control','readonly':'True'}),
                                     label="Enter your residence",
                                     required=True)
        floor=forms.CharField(widget=forms.TextInput
                                     (attrs={'class':'form-control','readonly':'True'}),
                                     label="Enter your Floor Number",
                                     required=True)
        owner_name=forms.CharField(widget=forms.TextInput
                                     (attrs={'class':'form-control','readonly':'True'}),
                                     label="Enter your Owner's Name",
                                     required=True)
        def clean_contact_no(self):
            print"pass check"
            print "i= pass_",self.cleaned_data
            cno1=self.cleaned_data['contact_no']
            cno=(str)(cno1)
            if len(cno) != 10:
                raise forms.ValidationError('Invalid contact number...!')
            else:
                return self.cleaned_data['contact_no']
        class Meta:
            model=flat_info
            fields=['contact_no','occupation','members','residence','floor','owner_name']
