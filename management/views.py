from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.shortcuts import *
from django.http import *
from .forms import *
from .models import *
from django.db.models import Q
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django import forms
from django.contrib import messages
from django.views.generic import CreateView
from django.conf import settings
from django.core.mail import send_mail
import datetime
from twilio.rest import Client
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.shortcuts import *
from django.http import *
from django.db.models import Q
from django.contrib import auth
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.views.generic import CreateView
from django import forms
from django_user_agents.utils import get_user_agent
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

#....................id pass for message....................

account_sid = ""
auth_token  = ""
client =Client(account_sid, auth_token)
#...........................................................
def dir(request):
    squery = flat_info.objects.all()
    print squery
    if squery:
        return render(request,'info.html',{'q':squery})
    else:
        return render(request,'info.html',{'q':squery})

def index(request):
    form=conform()
    form1=compform()
    no=notice.objects.order_by('-date_created')
    ev=event.objects.order_by('-date_created')
    print"notices",no
    if request.method=='POST':
            form=conform(request.POST)
            if form.is_valid():
                f=form.save(commit=False)
                print"email=-=",f
                email=(str)(f.email)
                f.save()
                print"form saved"
                #.........................email........................................
                to_email=[email]
                subject='NEELKANTH SOCIETY'
                message="Thank you...! We appreciate you for showing interest in Neelkanth Society .Will be in touch with you shortly."
                from_email=settings.EMAIL_HOST_USER
                send_mail(subject,
                          message,
                          from_email,
                          to_email,
                          fail_silently=False)
                print"mail sended"
                #......................................................................
                return render(request,'guestsuccess.html')

    else:
        form=conform()
        form1=compform()
    return render(request, "resihome.html",{'form1':form1,'form':form,'notice':no,'event':ev})

def cont(request):
    if request.method=='POST':
            form1=compform(request.POST)
            if form1.is_valid():
                print"in form1"
                f=form1.save(commit=False)
                print"form1.email=-=",f
                email=(str)(f.email)
                f.save()
                print"form saved"
                #.........................email........................................
                to_email=[email]
                subject='NEELKANTH SOCIETY'
                message="Thank you...! Your complaint is updated in our system....Will be in touch with you shortly."
                from_email=settings.EMAIL_HOST_USER
                send_mail(subject,
                          message,
                          from_email,
                          to_email,
                          fail_silently=False)
                print"mail sended"
                #......................................................................
                return render(request,'guestsuccess.html')
    else:
        form1=compform()
    return render(request, "complaint.html",{'form1':form1})

def home(request):
    if request.user.is_authenticated():
        user=request.user
        return render(request,'resihome.html',{'cu':user})
    else:
        return mlogin(request)

def search2(request):
    squery= request.POST['search_box']
    form=dir1()
    if squery:
        s = flat_info.objects.filter(flat_no__icontains=squery)
        if s:
            return render(request,'info.html',{'form':form,'q':s})
        else:
            return render(request,'info.html',{'form':form,'q':s})
