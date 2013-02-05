from django.conf import settings
from django.contrib.auth.models import Group, User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import F, Max, Q, connection
from django.template import RequestContext, Template, defaultfilters as filters
from django.template.context import Context


class UserProfile(models.Model):
    def get_absolute_url(self):
        return ('profiles_profile_detail', (), { 'username': self.user.username })
    get_absolute_url = models.permalink(get_absolute_url)
 
    SEX_CHOICES = (('male', 'Male'),
                   ('female', 'Female'))
    
    PREFERENCE_CHOICES = (('men', 'Men'),
                          ('women', 'Women'),
                          ('both', 'Both'))
                                  
        
    user = models.ForeignKey(User, unique=True)
    #url = models.URLField("Website", blank=True)
    sex = models.CharField(max_length=10, blank=True, choices=SEX_CHOICES)
    preference = models.CharField(max_length=10, blank=True, 
                                  choices=PREFERENCE_CHOICES)

class Place(models.Model):
    '''
    '''
    name = models.CharField(max_length=128)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    
    
class Vote(models.Model):
    user = models.ForeignKey(User, related_name='votes')
    place = models.ForeignKey(Place)
    ratio = models.IntegerField(default=50, 
                    help_text='Only Men 1, 25, 50, 75, 99  Only Women')
    hotness = models.IntegerField(default=0)
    
    
class VoteVerification(models.Model):
    user = models.ForeignKey(User, related_name='verifications')
    verified = models.BooleanField()
    
    
#TODO: Add comments to Vote (and verifications?)