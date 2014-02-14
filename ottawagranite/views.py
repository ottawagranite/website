from django.shortcuts import render_to_response
from ottawagranite import common
from membership.models import League

def leagues_landing_page(request):
    """Display the leagues landing page."""
    menus = common.main_menu()
    leagues = League.objects.all()
    return render_to_response('leagues.html',
        {
            "top_menus": menus,
            "leagues": leagues
        })

def life_members(request):
    menus = common.main_menu()
    return render_to_response('life_members.html',
        { "top_menus": menus })

def home(request):
    menus = common.main_menu()
    return render_to_response('index.html',
        { "top_menus": menus })

def about(request):
    """Display the about page."""
    menus = common.main_menu()
    return render_to_response('about.html',
        { "top_menus": menus })
