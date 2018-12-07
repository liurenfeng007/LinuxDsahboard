"""LinuxDsahboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, url
from django.conf import  settings
from django.contrib import admin

urlpatterns = patterns('',
                       # url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'main.views.index', name='index'),
                       url(r'^main/$', 'main.views.getall', name='main'),
                       url(r'^info/uptime/$', 'usage.views.uptime', name='uptime'),
                       url(r'^info/memory/$', 'usage.views.memusage', name='memusage'),
                       url(r'^info/cpuusage/$', 'usage.views.cpuusage', name='cpuusage'),
                       url(r'^info/getdisk/$', 'usage.views.getdisk', name='getdisk'),
                       url(r'^info/getips/$', 'usage.views.getips', name='getips'),
                       url(r'^info/gettraffic/$', 'usage.views.gettraffic', name='gettraffic'),
                       url(r'^info/proc/$', 'usage.views.getproc', name='getproc'),
                       url(r'^info/getdiskio/$', 'usage.views.getdiskio', name='getdiskio'),
                       url(r'^info/loadaverage/$', 'usage.views.loadaverage', name='loadaverage'),
                       url(r'^info/platform/([\w\-\.]+)/$', 'usage.views.platform', name='platform'),
                       url(r'^info/getcpus/([\w\-\.]+)/$', 'usage.views.getcpus', name='getcpus'),
                       url(r'^info/getnetstat/$', 'usage.views.getnetstat', name='getnetstat'))

urlpatterns += patterns('',
                        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                         {'document_root': settings.STATIC_ROOT}))
