from django.shortcuts import render_to_response
from ottawagranite import common

def home(request):
    menus = common.main_menu()
    return render_to_response('index.html',
        { "top_menus": menus })

def about(request):
    """Display the about page."""
    menus = common.main_menu()
    return render_to_response('about.html',
        { "top_menus": menus })
