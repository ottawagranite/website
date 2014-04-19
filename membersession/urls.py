from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.auth.views import password_change
from django.core.urlresolvers import reverse
from django.utils.functional import lazy

reverse_lazy = lazy(reverse, unicode)

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
    url(r'^changepassword/$',
        password_change,
            {
                'template_name': 'password_change_form.html',
                'post_change_redirect': reverse_lazy('home')
            },
        name='membersession-changepassword'),
)
