from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$',
        'login.views.login',
        name='login-login'),
)
