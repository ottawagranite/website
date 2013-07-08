from django.conf.urls import patterns, include, url
from django.conf import settings
import os

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

projdir = settings.PROJDIR

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ottawagranite.views.home', name='home'),
    # url(r'^ottawagranite/', include('ottawagranite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Serve static content
    url(r'^static/(?P<path>.*)',
         'django.views.static.serve',
         { 'document_root': os.path.abspath(os.path.join(projdir, 'static')) })
)
