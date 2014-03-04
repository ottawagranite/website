from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render_to_response
from django.template import RequestContext
from ottawagranite import common


def leagues_landing_page(request):
    """Display the leagues landing page."""
    return render_to_response('leagues.html',
        RequestContext(request, {
            }))

def life_members(request):
    return render_to_response('life_members.html',
        RequestContext(request, {
            }))

def home(request):
    return render_to_response('index.html',
        RequestContext(request, {
            }))

def about(request):
    """Display the about page."""
    return render_to_response('about.html',
        RequestContext(request, {
            }))
