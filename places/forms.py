from django.db import models
from django.forms import ModelForm
from places.models import Place
 
class ProfileForm(ModelForm):
  class Meta:
      model = Place
      exclude = ('field1','field2','field3',)