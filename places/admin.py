from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from places.models import UserProfile

from django.db.models import get_models, get_app
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

def autoregister(*app_list):
    for app_name in app_list:
        app_models = get_app(app_name)
        for model in get_models(app_models):
            try:
                admin.site.register(model)
            except AlreadyRegistered:
                pass
            
# register all models defined on each app
autoregister('places')


admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserProfileAdmin(UserAdmin):
    inlines = [ UserProfileInline, ]
    def sex(self, obj):
        try:
            return obj.get_profile().sex
        except UserProfile.DoesNotExist:
            return ''
        
    def roles(self, obj):
        groups = sorted([unicode(x) for x in obj.groups.all()])
        if obj.user_permissions.exists():
            groups.append('+')
        return mark_safe('<nobr>%s</nobr>' % ', '.join(groups))
    roles.allow_tags = True
    roles.short_description = u'Groups'
    
    def last_logged_in(self, obj):
        return mark_safe('<nobr>%s</nobr>' % obj.last_login.strftime('%b %d, %H:%M'))
    last_logged_in.admin_order_field = 'last_login'
    last_logged_in.allow_tags = True
    last_logged_in.short_description = u'Last Login'
        
    list_display = UserAdmin.list_display + ('roles', 'sex', 'last_logged_in')
    list_filter = UserAdmin.list_filter + ('groups', 'is_active', 'last_login')
    ordering = ['username']
    search_fields = UserAdmin.search_fields + ('userprofile__sex',)
    

admin.site.register(User, UserProfileAdmin)