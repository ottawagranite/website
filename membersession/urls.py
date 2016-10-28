from django.conf.urls import url
from django.conf import settings
from django.contrib.auth.views import password_change
from django.core.urlresolvers import reverse
from django.utils.functional import lazy
from membersession import views

reverse_lazy = lazy(reverse, unicode)

urlpatterns = [
    url(r'^manageaccount/$',
         views.manage_account,
         name='membersession-manageaccount'),
    url(r'^logout/$',
        views.member_logout,
        name='membersession-logout'),
    url(r'^$',
        views.member_login,
        name='membersession-login'),
    url(r'^changepassword/$',
        password_change,
            {
                'template_name': 'password_change_form.html',
                'post_change_redirect': reverse_lazy('home')
            },
        name='membersession-changepassword'),
]
