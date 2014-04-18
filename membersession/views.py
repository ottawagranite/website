from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render_to_response
from django.template import RequestContext
import logging, json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from membersession.forms import MemberForm

log = logging.getLogger(__name__)

@login_required
def manage_account(request):
    """Manage your account settings."""
    log.info("in membersession.views.manageaccount")
    form = MemberForm()
    if request.method == 'GET':
        log.debug('GET request')

    elif request.method == 'POST':
        log.debug('POST request')

    return render_to_response('account.html',
        RequestContext(request,
            {
                'form': form
            }))

def member_login(request):
    """Handle user logins."""
    log.info("in login")
    if request.method == 'POST':
        log.debug("POST request")
        try:
            j = json.loads(request.body)
        except Exception, err:
            log.error("JSON parse failure: %s", str(err))
            return HttpResponse(status=400)

        username = j.get('userid', 'unknown')
        password = j.get('password', 'unknown')
        log.info("login attempt for user %s", username)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                log.info("successful login for user %s", username)
                return HttpResponse('OK')

            else:
                log.error("user %s is disabled", username)
                return HttpResponse(status=403)

        else:
            log.error("invalid login for user %s", user)
            return HttpResponse(status=403)

    else:
        log.error("Unsupported HTTP request method: %s", request.method)
        return HttpResponse(status=400)

def member_logout(request):
    """Handle user logouts."""
    log.info("in logout")
    if request.method == 'POST':
        log.debug("POST request")
        logout(request)
        return HttpResponse('OK')

    else:
        log.error("Unsupported HTTP request method: %s", request.method)
        return HttpResponse(status=400)
