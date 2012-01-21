import cherrypy
import urllib.request
import urllib.parse

from . import constants
from . import user


def deauthenticate():
    cherrypy.response.cookie[constants.FACEBOOK_ACCESS_TOKEN] = cherrypy.request.cookie[constants.FACEBOOK_ACCESS_TOKEN]
    cherrypy.response.cookie[constants.FACEBOOK_ACCESS_TOKEN]['expires'] = 0

def authenticate(code):
    raw_access_data = str(urllib.request.urlopen("https://graph.facebook.com/oauth/access_token?" \
        "client_id=" + constants.APP_ID + "&redirect_uri=" + constants.CALLBACK_URL + \
        "&client_secret=" + constants.APP_SECRET + "&code=" + code).read(), encoding="utf-8")
    
    access_data = urllib.parse.parse_qs(raw_access_data)
    
    cherrypy.response.cookie[constants.FACEBOOK_ACCESS_TOKEN] = access_data['access_token']
    cherrypy.response.cookie[constants.FACEBOOK_ACCESS_TOKEN]['expires'] = access_data['expires']
    
    user.getUserId(access_data['access_token'])



