from django.conf.urls import url, include
from django.conf import settings
from django.views import static
import os
from django.contrib.auth import get_user_model
from registration.forms import RegistrationForm
from django.views.generic.base import TemplateView
from registration.backends.default.views import ActivationView, RegistrationView
from django import forms
from ottawagranite import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

projdir = settings.PROJDIR

# http://stackoverflow.com/questions/13568172/django-1-5-custom-user-model-error-manager-isnt-available-user-has-been-swap
class GraniteRegistrationForm(RegistrationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            get_user_model().objects.get(username=username)
        except get_user_model().DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

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

    # Django registration
    #url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/activate/complete/$',
         TemplateView.as_view(template_name='registration/activation_complete.html'),
         name='registration_activation_complete'),
    url(r'^accounts/activate/(?P<activation_key>\w+)/$',
         ActivationView.as_view(),
         name='registration_activate'),
    url(r'^accounts/register/$',
         RegistrationView.as_view(form_class=GraniteRegistrationForm),
         name='registration_register'),
    url(r'^accounts/register/complete/$',
         TemplateView.as_view(template_name='registration/registration_complete.html'),
         name='registration_complete'),
    url(r'^accounts/register/closed/$',
         TemplateView.as_view(template_name='registration/registration_closed.html'),
         name='registration_disallowed'),
    (r'accounts/', include('registration.auth_urls')),

    # Handle logins
    url(r'^membersession/', include('membersession.urls')),

    # Serve static content
    url(r'^static/(?P<path>.*)',
        static.serve,
        { 'document_root': settings.STATIC_ROOT })
]
