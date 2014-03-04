from django.conf.urls import patterns, include, url
from django.conf import settings
import os

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

projdir = settings.PROJDIR

urlpatterns = patterns('',
    url(r'leagues/$',
        'ottawagranite.views.leagues_landing_page',
        name='leagues-landing-page'),
    url(r'membership/life_members/$',
        'ottawagranite.views.life_members',
        name='life-members'),
    url(r'info/about/$', 'ottawagranite.views.about', name="about"),
    url(r'^$', 'ottawagranite.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),

    # Django registration
    url(r'^accounts/', include('registration.backends.default.urls')),

    # Handle logins
    url(r'^login/', include('login.urls')),

    # Serve static content
    url(r'^static/(?P<path>.*)',
        'django.views.static.serve',
        { 'document_root': settings.STATIC_ROOT })
)
