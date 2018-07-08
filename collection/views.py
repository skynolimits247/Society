from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.shortcuts import *
from django.http import *
from management.forms import *
from management.models import *
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
# Create your views here.
def index(request):
    print"in index"
    f=request.user
    return render(request,"manbasepage.html",{'cu':f});
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def mlogin(request):
    form=resiloginform()
    print"in here"
    return render(request,'login.html',{'form':form})
def auth_view(request):
    print"in auth view"
    username = request.POST['username']
    password = request.POST['password']
    print username,password
    user = auth.authenticate(username=username,password=password)
    print "user = ",user
    if user is not None:
        auth.login(request,user)
        user=request.user
        return render(request,'manbasepage.html',{'cu':user})
    else:
        return render(request,'invalid.html')

def maint(request):
        print"in maint"
        if request.user.is_authenticated():
            f=request.user
            if request.method=='POST':
                    cat=request.POST['category']
                    print "cat = ",cat
                    if cat=="Pay Maintenance":
                        return render(request,"search.html",{'cu':f})
                    elif cat=="View Paid Maintenances":
                        return render(request,'paidcategory.html',{'cu':f})
                    elif cat=="View Unpaid Maintenances":
                        return render(request,'unpaidinfo.html',{'cu':f})
            else:
                return render(request,"maintenancecategory.html",{'cu':f})
        else:
            return mlogin(request)

def home(request):
    print"in home"
    if request.user.is_authenticated():
        return index(request)
    else:
        return mlogin(request)
def cat(request):
    if request.user.is_authenticated():
        cu=request.user
        print"cu==",cu
        if request.method=='POST':
                cat=request.POST['category']
                print "cat = ",cat
                if cat=="Maintenance":
                    return render(request,'maintenancecategory.html',{'cu':cu})
                elif cat=="View Paid Maintenances":
                    return render(request,'paidcategory.html')
                elif cat=="Total Paid":
                    s=tid.objects.all()
                    return render(request,'paidinfo.html',{'q':s,'cu':cu})
                elif cat=="Total Paid":
                    s=tid.objects.all()
                    return render(request,'paidinfo.html',{'q':s,'cu':cu})
                elif cat=="Installments Paid":
                    print"in installments paid"
                    return render(request,'search1.html')
                    #s=maintenance.objects.all()
                    #return render(request,'installmentinfo.html',{'q':s})
                elif cat == "View Unpaid Maintenances":
                    s = tid.objects.all()
                    print "s=",s
                    return render(request, 'unpaidinfo.html', {'q': s,'cu':cu})
    else:
        return mlogin(request)
def search(request):
    f=request.user
    if request.user.is_authenticated():
        squery= request.POST['search_box']

        if squery:
            s = flat_info.objects.filter(flat_no__icontains=squery)
            if s:
                return render(request,'detail.html',{'q':s,'cu':f})
            else:
                return render(request,'detail.html',{'q':s,'cu':f})
        else:
            return HttpResponseRedirect('/col/maint/')
    else:
        return mlogin(request)
def pay(request,d1):
    cu=request.user
    owner=flat_info.objects.get(flat_no=d1)
    t=tid.objects.get(flat_no=d1)
    form1=maintenance_type.objects.all()
    if request.user.is_authenticated():
        form1=maintenance_type.objects.all()
        if request.method=='POST':
            form = detail(request.POST);
            print"created form"
            if form.is_valid():
                n=0
                amt1=0
                fine1=0
                s=0
                amount=0
                fine=0
                amt=0
                print"in validation"
                f=form.save(commit=False)
                f.flat_no=d1
                ins=f.type_of_maintenance
                print"type = ",f.type_of_maintenance
                d=maintenance_type.objects.get(maintenance_header__exact=ins)
                z=(d.counter)
                f.fine=0
                print "d= ",d
                s=(str)(f.type_of_maintenance)
                f.amount=d.amount
                amt=f.amount
                #...............................amount update...........................................
                if("Maintenance" in s):
                    print"in maintenance_type if"
                    n=(f.maintenance_counter)
                    print"n+z=",n+z
                    n=n+z
                    print"f.counter= ",f.maintenance_counter
                    print"f.amount= ",f.amount
                    print"form saved"
                    n=n+t.maintenance_count
                    count=t.maintenance_count
                    f.maintenance_counter=n
                    print "n= ",n

                if("Sinking" in s):
                    n=(f.sinkingfund_counter)
                    print"n+z=",n+z
                    n=n+z
                    print"f.counter= ",f.sinkingfund_counter
                    print"f.amount= ",f.amount
                    print"form saved"
                    print"t.sinkingfund = ",t.sinkingfund_count
                    n=n+t.sinkingfund_count
                    count = t.sinkingfund_count
                    f.sinkingfund_counter=n
                    print "n= ",n

                if("Parking" in s):
                    n=(f.parking_counter)
                    print"n+z=",n+z
                    n=n+z
                    print"f.counter= ",f.parking_counter
                    print"f.amount= ",f.amount
                    print"form saved"
                    n=n+t.parking_count
                    count = t.parking_count
                    f.parking_counter=n
                    print "n= ",n
                #...............................fine...................................
                f.fine=0.0
                fine = (int)(f.fine)
                f1 = (int)(f.amount)
                #e = tid.objects.get(flat_no=d1)
                #c = e.count  # updated counter of tid table
                dat = datetime.date.today()
                m = (int)(dat.month)  # current month in int
                count = count % 1
                print "counter", count
                print "month", m
                if (count == 0 and not (m == 1)):
                    print"in 0"
                    fine = f1 * 0.05 * (m - 1)
                elif (count == 0.25 and not (m == 4)):
                  print"in .25"
                  if(m<4):
                    fine=0
                  else:
                    fine = f1 * 0.05 * (m - 4)
                elif (count == 0.50 and not (m == 7)):
                    print"in .50"
                    if (m < 7):
                        fine = 0
                    else:
                        fine = f1 * 0.05 * (m - 7)
                elif (count == 0.75 and not (m == 10)):
                    print"in .75"
                    if (m < 10):
                        fine = 0
                    else:
                        fine = f1 * 0.05 * (m - 10)
                f.fine = fine
                print "fine=", fine
                #......................................................................
                print"form=",f,f.flat_no,f.amount,f.fine,f.total_amount
                if("Maintenance" in s):
                    print"in maintenance_type if"
                    n=(f.maintenance_counter)
                    amt1=t.maintenance_paid
                    amt1+=amt
                    fine1=t.maintenance_fine_paid
                    fine1+=fine
                    tid.objects.filter(flat_no=f.flat_no).update(maintenance_count=n,last_id=f.id,maintenance_paid=amt1,maintenance_fine_paid=fine1)

                if("Sinking" in s):
                    n=(f.sinkingfund_counter)
                    amt1=t.sinkingfund_paid
                    amt1+=amt
                    fine1=t.sinkingfund_fine_paid
                    fine1+=fine
                    tid.objects.filter(flat_no=f.flat_no).update(sinkingfund_count=n,last_id=f.id,sinkingfund_paid=amt1,sinkingfund_fine_paid=fine1)

                if("Parking" in s):
                    n=(f.parking_counter)
                    amt1=t.parking_paid
                    amt1+=amt
                    fine1=t.parking_fine_paid
                    fine1+=fine
                    tid.objects.filter(flat_no=f.flat_no).update(parking_count=n,last_id=f.id,parking_paid=amt1,parking_fine_paid=fine1)
                amount = f.amount + f.fine
                #...............................amount update...........................................
                f.total_amount=f.amount+f.fine
        #.................................SMS sending.........................................
                text = 'NeelKanth Society : Payment Recieved from Flat Number : ' + (str)(owner.flat_no) + ' Regarding ' + (
                str)(f.type_of_maintenance) + " of amount Rs." + (str)(f.total_amount) + "Thank you..!!"
                to = "+91" + (str)(owner.contact_no)
                email=(str)(owner.email)
                print "messge = ", text
                message = client.messages.create(from_="+1 910-249-4565  ",
                                                 to=to,
                                                 body=text)

                form=detail(request.POST)
                f.total_amount=amount+fine
                form=detail(instance=f)
                #.........................email........................................
                to_email=[email]
                subject='payment receipt'
                message=text
                from_email=settings.EMAIL_HOST_USER
                send_mail(subject,
                          message,
                          from_email,
                          to_email,
                          fail_silently=False)
                print"mail sended"
                #......................................................................
                form=detail(instance=f)
                flag=1
                f.save()
                return render(request,'payment1.html',{'form':form,'cu':cu,'i':t})

        else:
            print"in else"
            form=detail()
            return render(request,'payment.html',{'form':form,'form1':form1,'cu':cu,'t':t})

        return render(request,'payment.html',{'form':form,'form1':form1,'cu':cu,'t':t})
    else:
        return mlogin(request)

def search1(request):
    cu=request.user
    if request.user.is_authenticated():
        squery= request.POST['search_box']
        if squery:
            s = maintenance.objects.filter(flat_no__icontains=squery)
            if s:
                return render(request,'installmentinfo.html',{'q':s,'cu':cu})
            else:
                return render(request,'installmentinfo.html',{'q':s,'cu':cu})
        else:
            return mlogin(request)
def search0(request):
    cu=request.user
    if request.user.is_authenticated():
        squery= request.POST['search_box']
        if squery:
            s =flat_info.objects.get(flat_no__icontains=squery)
            print"s===",s.flat_no
            n=(int)(s.flat_no)
            if s:
                print"in if search0"
                return render(request,'updateinfo.html',{'q':s,'cu':cu})
            else:
                messages.error(request, 'Sorry no result found...!')
        else:
            return mlogin(request)
def addflat(request):
    f=request.user
    if request.user.is_authenticated():
        if request.method=='POST':
                form=Editflatinfoforms(request.POST)
                if form.is_valid():
                    f1=form.save(commit=False)
                    print"flat_no==",f1.flat_no
                    t=tid.objects.create(flat_no=(str)(f1.flat_no))
                    #.........................email........................................
                    to_email=[f1.email]
                    subject='Registered in Neelkanth Society'
                    message="Welcome "+(str)(f1.owner_name)+" your email is registered with flat number "+(str)(f1.flat_no)+" with your contact number as "+(str)(f1.contact_no)+" THANK YOU.....!!!!"
                    from_email=settings.EMAIL_HOST_USER
                    send_mail(subject,
                              message,
                              from_email,
                              to_email,
                              fail_silently=False)
                    print"mail sended"
                    #......................................................................
                    f1.save()
                    return render(request,'addflatsuccess.html',{'cu':f})
        else:
            form=Editflatinfoforms()
        return render(request,'addflat.html',{'form':form,'cu':f})
    else:
        return mlogin(request)
def upflat(request,d):
    f=request.user
    if request.user.is_authenticated():
        if request.method=='POST':
                form=Editflatinfo(request.POST)
                ins=flat_info.objects.get(flat_no=d)
                ins.delete()
                if form.is_valid():
                    f1=form.save(commit=False)
                    print"flat_no==",f1.flat_no

                    flat_info.objects.create(flat_no=f1.flat_no,owner_name=f1.owner_name,contact_no=f1.contact_no,occupation=f1.occupation,members=f1.members,email=f1.email,floor=f1.floor,residence=f1.residence)
                    #.........................email........................................
                    to_email=[f1.email]
                    subject='Information updated in Neelkanth Society'
                    message="Welcome "+(str)(f1.owner_name)+" your email is registered with flat number "+(str)(f1.flat_no)+" with your contact number as "+(str)(f1.contact_no)+" THANK YOU.....!!!!"
                    from_email=settings.EMAIL_HOST_USER
                    send_mail(subject,
                              message,
                              from_email,
                              to_email,
                              fail_silently=False)
                    print"mail sended"
                    #......................................................................
                    return render(request,'addflatsuccess.html',{'cu':f})
        else:
            s=flat_info.objects.get(flat_no=d)
            form=Editflatinfo(instance = s)
        return render(request,'addflat.html',{'form':form,'cu':f})
    else:
        return mlogin(request)

def ss(request):
        cu=request.user
        if request.user.is_authenticated():
            return render(request,'search0.html',{'cu':cu})
        else:
            return mlogin(request)
