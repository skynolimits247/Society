from __future__ import unicode_literals
from django.test import TestCase
from django import forms
from .models import *
from .views import *
from django.db import models
from django.contrib.auth.models import User
from .models import flat_info
from django.contrib.auth.models import AbstractUser
from .models import *

class detail(forms.ModelForm):
    class Meta:
        model=maintenance
        fields= ['flat_no','type_of_maintenance','amount','fine','financial_year']
class Editflatinfoforms(forms.ModelForm):
        email=forms.EmailField(widget=forms.TextInput
                              (attrs={'class':'panel'}),
                              label="Enter your Email",
                              required=True)
        owner_name=forms.CharField(widget=forms.TextInput
                                     (attrs={'class':'panel'}),
                                     label="Enter your Owner's Name",
                                     required=True)
        flat_no=forms.CharField(widget=forms.TextInput
                                     (attrs={'class':'panel'}),
                                     label="Enter your Flat Number",
                                     required=True)

        contact_no=forms.CharField(widget=forms.TextInput
                                     (attrs={'class':'panel'}),
                                     label="Enter your Contact Number",
                                     required=True)
        occupation=forms.CharField(widget=forms.TextInput
                                     (attrs={'class':'panel'}),
                                     label="Enter your Occupation",
                                     required=True)
        members=forms.CharField(widget=forms.TextInput
                                     (attrs={'class':'panel'}),
                                     label="Enter the number of family members",
                                     required=True)
        residence=forms.CharField(widget=forms.TextInput
                                     (attrs={'class':'panel'}),
                                     label="Enter your residence",
                                     required=True)
        floor=forms.CharField(widget=forms.TextInput
                                     (attrs={'class':'panel'}),
                                     label="Enter your Floor Number",
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
            fields=['contact_no','occupation','members','residence','floor','owner_name','email','flat_no']

class Editflatinfo(forms.ModelForm):
        email=forms.EmailField(widget=forms.TextInput
                              (attrs={'class':'panel'}),
                              label="Enter your Email",
                              required=True)
        owner_name=forms.CharField(widget=forms.TextInput
                                     (attrs={'class':'panel'}),
                                     label="Enter your Owner's Name",
                                     required=True)
        flat_no=forms.CharField(widget=forms.TextInput
                                     (attrs={'class':'panel','readonly':'True'}),
                                     label="(Read-Only) Flat Number",
                                     required=True)

        contact_no=forms.CharField(widget=forms.TextInput
                                     (attrs={'class':'panel'}),
                                     label="Enter your Contact Number",
                                     required=True)
        occupation=forms.CharField(widget=forms.TextInput
                                     (attrs={'class':'panel'}),
                                     label="Enter your Occupation",
                                     required=True)
        members=forms.CharField(widget=forms.TextInput
                                     (attrs={'class':'panel'}),
                                     label="Enter the number of family members",
                                     required=True)
        residence=forms.CharField(widget=forms.TextInput
                                     (attrs={'class':'panel','readonly':'True'}),
                                     label="(Read-Only) Residence",
                                     required=True)
        floor=forms.CharField(widget=forms.TextInput
                                     (attrs={'class':'panel','readonly':'True'}),
                                     label="(Read-Only) Floor Number",
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
            fields=['contact_no','occupation','members','residence','floor','owner_name','email','flat_no']

class resiloginform(forms.ModelForm):
    email=forms.EmailField(widget=forms.TextInput
                          (attrs={'class':'form-control'}),
                          label="Enter your Email",
                          required=True)
    password=forms.CharField(widget=forms.PasswordInput
                             (attrs={'class':'form-control'}),
                             label="Type your password",
                             max_length=30,
                             required=True)
    def clean_email(self):
        umail=self.cleaned_data['email']
        email=(str)(umail)
        try:
            match=onwer.objects.get(email=email)
            print "match=",match
        except:
            return self.cleaned_data['email']
        raise forms.ValidationError('email already registered..!!')
    class Meta:
        model=management
        fields=['email','password']

class dir1(forms.ModelForm):
    class Meta:
        model=flat_info
        fields= ['flat_no','owner_name','contact_no','occupation','email']

class conform(forms.ModelForm):
    umail="hello"
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
        fields=['email','name','query']

class compform(forms.ModelForm):
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
    flat_no=forms.CharField(widget=forms.TextInput
                             (attrs={'class':'panel','length':'100'}),
                             label="Enter your Flat Number",
                             required=True)

    def clean_email(self):
        mail=self.cleaned_data['email']
        print"in clean email form1",mail
        umail=(str)(mail)
        try:
            print "in try="
            match=flat_info.objects.get(email=umail)
            print "match=",match
            return self.cleaned_data['email']
        except:
            print"in except"
            raise forms.ValidationError('Email not registered..Please contact Society to update your Email Address....!!')
        raise forms.ValidationError('Email not registered..Please contact Society to update your Email Address....!!')

    def clean_flat_no(self):
        print"in clean email flat no"
        try:
            fno=self.cleaned_data['flat_no']
            umail=self.cleaned_data['email']
            print"in try2"
            match=flat_info.objects.get(flat_no=fno)
            print "match.email=",match.email
            email=(str)(match.email)
            print"email",email
            if email == umail :
                print"in if"
                return self.cleaned_data['flat_no']
            else :
                print"in else"
                raise forms.ValidationError('Flat number not registered with the email address.....Please contact Society to update your flat number....!!')
        except:
            print"in 2 except"
            raise forms.ValidationError('Flat number not registered with the email address.....Please contact Society to update your flat number....!!')
        raise forms.ValidationError('Email not registered..Please contact Society to update your Email Address....!!')
    class Meta:
        model=complaint
        fields=['email','name','flat_no','complaint_sub','complaint_details']

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
        fields=['flat_no','complaint_sub','complaint_details','complaint_status','email']

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
