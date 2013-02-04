from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from django.core.urlresolvers import reverse
from django.db import connection
from django.db.models import Count
from django.db.models.aggregates import Min
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic.simple import direct_to_template

def home(request):
  return direct_to_template(request, 'content/index.html')


@login_required
def view_profile(request):
    user_profile = request.user.get_profile()
    
    
def page_not_found(request):
    return direct_to_template(request, '404.html')