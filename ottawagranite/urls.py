from django.conf.urls import url, include
from django.conf import settings
from django.views import static
import os
from django.contrib.auth import get_user_model
from django.views.generic.base import TemplateView
from django import forms
from ottawagranite import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

projdir = settings.PROJDIR

urlpatterns = [
    url(r'leagues/$',
        views.leagues_landing_page,
        name='leagues-landing-page'),
    url(r'membership/life_members/$',
        views.life_members,
        name='life-members'),
    url(r'info/about/$', views.about, name="about"),
    url(r'^$', views.home, name='home'),

    url(r'^admin/', include(admin.site.urls)),

    # Handle logins
    url(r'^membersession/', include('membersession.urls')),

    # Serve static content
    url(r'^static/(?P<path>.*)',
        static.serve,
        { 'document_root': settings.STATIC_ROOT })
]
