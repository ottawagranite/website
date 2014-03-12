from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render_to_response
from django.template import RequestContext
from ottawagranite import common
import logging

log = logging.getLogger(__name__)

def leagues_landing_page(request):
    """Display the leagues landing page."""
    log.info("in leagues_landing_page")
    return render_to_response('leagues.html',
        RequestContext(request, {
            }))

def life_members(request):
    log.info("in life_members")
    return render_to_response('life_members.html',
        RequestContext(request, {
            }))

def home(request):
    log.info("in home")
    return render_to_response('index.html',
        RequestContext(request, {
            }))

def about(request):
    log.info("in about")
    """Display the about page."""
    return render_to_response('about.html',
        RequestContext(request, {
            }))
