#from django.conf import settings
from django.contrib.auth.models import User
#from django.core.urlresolvers import reverse
from django.db import models
#from django.db.models import F, Max, Q, connection
#from django.template import RequestContext, Template, defaultfilters as filters
#from django.template.context import Context


##class CustomUserManager(models.Manager):
    ##def create_user(self, username, email):
        ##return self.model._default_manager.create(username=username)


##class CustomUser(models.Model):
    ### Define a custom User class to work with django-social-auth
    ##username = models.CharField(max_length=128)
    ##last_login = models.DateTimeField(blank=True, null=True)

    ##objects = CustomUserManager()

    ##def is_authenticated(self):
        ##return True
    

class UserProfile(models.Model):
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
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return '%s (%s)' % (self.user, self.sex)
    
    def get_absolute_url(self):
        return ('profiles_profile_detail', (), { 'username': self.user.username })
    get_absolute_url = models.permalink(get_absolute_url)
 

class Place(models.Model):
    name = models.CharField(max_length=128)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    
    def __unicode__(self):
        return '%s' % (self.name)    
    

class Vote(models.Model):
    place = models.ForeignKey(Place)
    user = models.ForeignKey(User, related_name='votes')
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    ratio = models.IntegerField(default=50, 
                    help_text='Only Men | 1%, 25%, 50%, 75%, 99% | Only Women')
    hotness = models.IntegerField(default=50,
                    help_text='Minger | 0%, 25%, 50%, 75%, 100% | Hot')
    
    def __unicode__(self):
        return '%s: %d%% women %d%% hot (%s)' % (
            self.place, self.ratio, self.hotness, self.user)
    
    
class VoteVerification(models.Model):
    user = models.ForeignKey(User, related_name='verifications')
    verified = models.BooleanField()
    
    def __unicode__(self):
        return '%s (%s)' % (self.user, self.verified)
    
    
#TODO: Add comments to Vote (and verifications?)