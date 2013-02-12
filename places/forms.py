#from django.db import models
from django.forms import ModelForm
from places.models import Place, Vote

class ProfileForm(ModelForm):
    class Meta:
        model = Place
        exclude = ('field1','field2','field3',)
      
      
class VoteForm(ModelForm):
    class Meta:
        model = Vote
        exclude = ('user',)