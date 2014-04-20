from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render_to_response
from django.template import RequestContext
import logging, json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from membersession.forms import MemberForm
from django.contrib import messages
from django.core.urlresolvers import reverse
from curling.models import League, Player, TeamPlayer
from django.core.exceptions import ValidationError, ObjectDoesNotExist

log = logging.getLogger(__name__)

def update_leagues(request):
    """Manage the league memberships requested by the user."""
    user = request.user
    league_names_requested = [name[7:] for name in request.POST
                                if name.startswith('league-')]
    log.info("found these requested leagues: %s", league_names_requested)
    # FIXME: need to check that the user can join these leagues.
    if league_names_requested:
        # Does this user have a player object? If they do, use the first one.
        try:
            player = user.player

        except ObjectDoesNotExist:
            log.debug("creating Player")
            player = Player()
            user.player = player
            player.first_name = user.first_name
            player.last_name = user.last_name
            player.gender = user.gender
            player.save()
            user.save()

        for league_name in league_names_requested:
            try:
                league = League.objects.get(name=league_name)
            except League.DoesNotExist:
                log.error("form requested a league that doesn't exist: %s", league_name)
                # FIXME: report this automatically via email
                messages.error(request, "Internal error - report this immediately")
                raise ValidationError, "League %s does not exist" % league_name

            # In this league already?
            if player.in_league(league):
                log.debug("player %s is in league %s already", player, league)
            else:
                log.debug("not yet in league %s, adding", league)
                teamplayer = TeamPlayer()
                teamplayer.position = 'Undecided'
                teamplayer.player = player
                teamplayer.league = league
                teamplayer.save()

@login_required
def manage_account(request):
    """Manage your account settings."""
    log.info("in membersession.views.manageaccount")
    all_leagues = League.objects.all()
    try:
        user_league_names = [league.name for league in request.user.player.get_leagues()]
    except ObjectDoesNotExist:
        user_league_names = []

    if request.method == 'GET':
        log.debug('GET request')
        form = MemberForm(instance=request.user)

    elif request.method == 'POST':
        log.debug('POST request')
        form = MemberForm(instance=request.user, data=request.POST)
        try:
            update_leagues(request)
        except Exception, err:
            # FIXME: report this automatically
            log.error("update_leagues: %s", str(err))
            messages.error(request, str(err))
            return HttpResponseRedirect(reverse('membersession-manageaccount'))

        if form.is_valid():
            form.save()
            messages.success(request, "Account successfully updated")
            return HttpResponseRedirect(reverse('home'))
        
        else:
            log.warn("form is not valid: %s" % form.errors)
            messages.error(request, "Please fix the errors below")

    return render_to_response('account.html',
        RequestContext(request,
            {
                'form': form,
                'all_leagues': all_leagues,
                'user_league_names': user_league_names
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
