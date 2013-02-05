from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from places.forms import ProfileForm

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'places.views.home', name='home'),
    #url('^profiles/edit', 'profiles.views.edit_profile', 
        #{'form_class': ProfileForm,
         ##'success_url':'/my/custom/url',
         #}),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    
    url(r'', include('social_auth.urls')),  #All django-social-auth URLs names have socialauth_ prefix.



    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    

    url(r'^admin/', include(admin.site.urls)),

    # WARNING: Not production-friendly!
    url(r'^sentry/', include('sentry.web.urls')),
)

urlpatterns += patterns('django.views.generic.simple',
    (r'crossdomain.xml', 'direct_to_template', {'template': 'staticfiles/crossdomain.xml'}),
    (r'robots.txt', 'direct_to_template', {'template': 'staticfiles/robots.txt'}),
)