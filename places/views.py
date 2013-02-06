from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from django.core.urlresolvers import reverse
from django.db import connection
from django.db.models import Count
from django.db.models.aggregates import Min
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic.simple import direct_to_template

from social_auth import __version__ as social_auth_version
from social_auth.utils import setting

def home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return HttpResponseRedirect('done')
    else:
        return render_to_response('social_auth/home.html', {},
                                  RequestContext(request))


def page_not_found(request):
    return direct_to_template(request, '404.html')
  
@login_required
def view_profile(request):
    user_profile = request.user.get_profile()
    


@login_required
def done(request):
    """Login complete view, displays user data"""
    ctx = {
        'version': version,
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