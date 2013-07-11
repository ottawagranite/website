from django.shortcuts import render_to_response
from ottawagranite import common

def home(request):
    menus = common.main_menu()
    return render_to_response('index.html',
        { "top_menus": menus })
