from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('membersession.views',
    url(r'^manageaccount/$',
         'manage_account',
         name='membersession-manageaccount'),
    url(r'^logout/$',
        'member_logout',
        name='membersession-logout'),
    url(r'^$',
        'member_login',
        name='membersession-login'),
)
