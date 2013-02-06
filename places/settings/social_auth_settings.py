
# Social Auth Settings
DAILYMOTION_OAUTH2_KEY             = ''
DAILYMOTION_OAUTH2_SECRET          = ''
FACEBOOK_APP_ID                    = ''
FACEBOOK_API_SECRET                = ''
FOURSQUARE_CONSUMER_KEY            = ''
FOURSQUARE_CONSUMER_SECRET         = ''
GOOGLE_CONSUMER_KEY                = ''
GOOGLE_CONSUMER_SECRET             = ''
GOOGLE_OAUTH2_CLIENT_ID            = ''
GOOGLE_OAUTH2_CLIENT_SECRET        = ''
LINKEDIN_CONSUMER_KEY              = ''
LINKEDIN_CONSUMER_SECRET           = ''
LIVE_CLIENT_ID                     = ''
LIVE_CLIENT_SECRET                 = ''
MAILRU_OAUTH2_CLIENT_KEY           = ''
MAILRU_OAUTH2_APP_KEY              = ''
MAILRU_OAUTH2_CLIENT_SECRET        = ''
ODNOKLASSNIKI_OAUTH2_CLIENT_KEY    = ''
ODNOKLASSNIKI_OAUTH2_APP_KEY       = ''
ODNOKLASSNIKI_OAUTH2_CLIENT_SECRET = ''
ORKUT_CONSUMER_KEY                 = ''
ORKUT_CONSUMER_SECRET              = ''
READABILITY_CONSUMER_KEY           = ''
READABILITY_CONSUMER_SECRET        = ''
SHOPIFY_APP_API_KEY                = ''
SHOPIFY_SHARED_SECRET              = ''
SKYROCK_CONSUMER_KEY               = ''
SKYROCK_CONSUMER_SECRET            = ''
STOCKTWITS_CONSUMER_KEY            = ''
STOCKTWITS_CONSUMER_SECRET         = ''
TWITTER_CONSUMER_KEY               = ''
TWITTER_CONSUMER_SECRET            = ''
VKONTAKTE_APP_ID                   = ''
VKONTAKTE_APP_SECRET               = ''
# Usage for applications auth: {'key': application_key, 'user_mode': 0 (default) | 1 (check) | 2 (online check) }
# 0 means is_app_user request parameter is ignored, 1 - must be = 1, 2 - checked via VK API request (useful when user
# connects to your application on app page and you reload the iframe)
#VKONTAKTE_APP_AUTH={'key':'iframe_app_secret_key', 'user_mode': 2, 'id':'iframe_app_id'}
YAHOO_CONSUMER_KEY                 = ''
YAHOO_CONSUMER_SECRET              = ''
YANDEX_OAUTH2_CLIENT_KEY           = ''
YANDEX_OAUTH2_CLIENT_SECRET        = ''
YANDEX_OAUTH2_API_URL              = 'https://api-yaru.yandex.ru/me/' # http://api.moikrug.ru/v1/my/ for Moi Krug



# Login URLs
LOGIN_URL          = '/login-form/'
LOGIN_REDIRECT_URL = '/logged-in/'
LOGIN_ERROR_URL    = '/login-error/'

#TODO: Invite new users to edit their profile
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/new-users-redirect-url/'
SOCIAL_AUTH_COMPLETE_URL_NAME     = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME    = 'socialauth_associate_complete'
#SOCIAL_AUTH_USER_MODEL           = 'app.CustomUser'

SOCIAL_AUTH_CREATE_USERS          = True
SOCIAL_AUTH_FORCE_RANDOM_USERNAME = False
SOCIAL_AUTH_FORCE_POST_DISCONNECT = True

import random
#SOCIAL_AUTH_DEFAULT_USERNAME      = 'socialauth_user'
SOCIAL_AUTH_DEFAULT_USERNAME       = lambda: random.choice(['Darth Vader', 'Obi-Wan Kenobi', 'R2-D2', 'C-3PO', 'Yoda'])


SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.misc.save_status_to_session',
    'app.pipeline.redirect_to_form',
    'app.pipeline.username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',

    #'social_auth.backends.pipeline.misc.save_status_to_session',
    #'app.pipeline.redirect_to_form2',
    #'app.pipeline.first_name',
)

