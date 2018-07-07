"""appt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from .import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'mlogin/$', views.mlogin, name='mlogin'),
    url(r'logout/$',views.logout),
    url(r'check/$',views.auth_view),
    url(r'maint/$',views.maint),
    url(r'home/$',views.home),
    url(r'cat/$',views.cat),
    url(r'addflat/$',views.addflat),
    url(r'upflat/(\d+)/$',views.upflat),
    url(r'search/$',views.search),
    url(r'search1/$',views.search1),
    url(r'ss/$',views.ss),
    url(r'search0/$',views.search0),
    url(r'pay/(\d+)/$',views.pay, name='pay'),
    #url(r'pay1/(\d+)/$',views.pay1, name='pay1'),
    #url(r'home/$',views.home),
    #url(r'cont/$',views.cont),
    #url(r'mprofile/(\d+)/$',views.mprofile),

]
