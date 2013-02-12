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
    
    # content
    url(r'^hot-places/', hot_places, name='hot_places'),
    url(r'^vote/(?P<id>\d+)?', vote, name='vote'),
    
    # API
    url(r'^api/', include(venues_resource.urls)),
    

    # authentication
    url(r'^done/$', done, name='done'),
    ##url(r'^error/$', error, name='error'),
    url(r'^logged-in/$', logged_in, name='logged_in'),
    url(r'^login-error/$', error, name='error'),
    url(r'^logout/$', logout, name='logout'),
    ##url(r'^form/$', form, name='form'),
    ##url(r'^form2/$', form2, name='form2'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^fb/', facebook_view, name='fb_app'),
    ##url(r'^vk/', vkontakte_view, name='vk_app'),
    ##url(r'^ok/$', ok_app, name='ok_app'),
    ##url(r'^ok/info/$', ok_app_info, name='ok_app_info'),
    url(r'^close_login_popup/$', close_login_popup, name='login_popup_close'),
    
    
    url(r'', include('social_auth.urls')),  #All django-social-auth URLs names have socialauth_ prefix.
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sentry/', include('sentry.web.urls')),  # WARNING: Not production-friendly!
)

urlpatterns += patterns('django.views.generic.simple',
    (r'crossdomain.xml', 'direct_to_template', {'template': 'staticfiles/crossdomain.xml'}),
    (r'robots.txt', 'direct_to_template', {'template': 'staticfiles/robots.txt'}),
)