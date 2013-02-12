from datetime import datetime, timedelta

#from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required #, permission_required
from django.contrib.messages.api import get_messages
from django.core.urlresolvers import reverse
#from django.db import connection
from django.db.models import Avg, Count #, Sum
#from django.db.models.aggregates import Min
from django.http import HttpResponseRedirect #HttpResponse, 
from django.shortcuts import render_to_response #, redirect
from django.template import RequestContext
from django.views.generic.simple import direct_to_template

from social_auth import __version__ as social_auth_version
#from social_auth.utils import setting

from places.models import Place, Vote
from places.forms import VoteForm

def page_not_found(request):
    return direct_to_template(request, '404.html')


def home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return HttpResponseRedirect('done')
    else:
        return render_to_response('social_auth/home.html', {},
                                  RequestContext(request))


def hot_places(request):
    '''
    '''
    newer_than = datetime.now() - timedelta(days=10)  # recent votes only
    hot_places = Place.objects.filter(vote__created__gte=newer_than).annotate(heat=Avg('vote__hotness'), vote_count=Count('vote')).order_by('-heat')[:10]
    return render_to_response('content/hot-places.html', 
                              {'hot_places': hot_places},
                              RequestContext(request))


@login_required
def vote(request, id=None):
    '''
    User can vote via POST - and edit their votes
    
    TODO: Page where user can see recent votes to edit their score
    TODO: Disallow more than one vote per place per hour
    '''
    form_args = {}
    if id is not None:
        # edit an existing Yazilar
        try:
            vote = Vote.objects.get(pk=id)
        except Vote.DoesNotExist:
            return Http404('Existing vote %d not found' % id)
        form_args['instance'] = vote
    # else create new vote

    if request.POST:
        # save form
        form_args['data'] = request.POST
        vote_form = VoteForm(**form_args)
        if vote_form.is_valid():
            vote = vote_form.save(commit=False)  # wait until we've added user
            vote.user = request.user
            vote.save()
            messages.success(request, 'Thanks for voting!')
    else:
        vote_form = VoteForm(**form_args)

    return render_to_response('content/vote.html',
        {
            'vote_form': vote_form
        },
        context_instance=RequestContext(request)
    )

def logged_in(request):
    '''
    once logged in, for now we'll take them to the main page
    '''
    return HttpResponseRedirect(reverse(hot_places))
#@login_required
#def view_profile(request):
    #user_profile = request.user.get_profile()
    


@login_required
def done(request):
    """Login complete view, displays user data"""
    ctx = {
        'version': social_auth_version,
        'last_login': request.session.get('social_auth_last_login_backend')
    }
    return render_to_response('social_auth/done.html', ctx, RequestContext(request))


def error(request):
    """Error view"""
    messages = get_messages(request)
    return render_to_response('social_auth/error.html', {'version': social_auth_version,
                                                         'messages': messages},
                              RequestContext(request))


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')


def close_login_popup(request):
    return render_to_response('close_popup.html', {}, RequestContext(request))
  
#def form(request):
    #if request.method == 'POST' and request.POST.get('username'):
        #name = setting('SOCIAL_AUTH_PARTIAL_PIPELINE_KEY', 'partial_pipeline')
        #request.session['saved_username'] = request.POST['username']
        #backend = request.session[name]['backend']
        #return redirect('socialauth_complete', backend=backend)
    #return render_to_response('form.html', {}, RequestContext(request))


#def form2(request):
    #if request.method == 'POST' and request.POST.get('first_name'):
        #request.session['saved_first_name'] = request.POST['first_name']
        #name = setting('SOCIAL_AUTH_PARTIAL_PIPELINE_KEY', 'partial_pipeline')
        #backend = request.session[name]['backend']
        #return redirect('socialauth_complete', backend=backend)
    #return render_to_response('form2.html', {}, RequestContext(request))



  
#you can do:
# user.social_auth.filter(provider='facebook') 
#and use the access_token stored in extra_data to talk with Facebook API. 