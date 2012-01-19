import cherrypy

from . import constants


CALLBACK_URL = "http://dns-dig.net/authenticatecallback"

def deauthenticate():
    cherrypy.response.cookie[constants.FACEBOOK_ACCESS_TOKEN] = cherrypy.request.cookie[constants.FACEBOOK_ACCESS_TOKEN]
    cherrypy.response.cookie[constants.FACEBOOK_ACCESS_TOKEN]['expires'] = 0

def authenticate():
    raise cherrypy.HTTPRedirect("https://graph.facebook.com/oauth/access_token?" \
        "client_id=" + constants.APP_ID + "&redirect_uri=" + CALLBACK_URL + \
        "client_secret=" + constants.APP_SECRET + "&code=" + cherrypy.response.cookie[constants.FACEBOOK_CODE])
    
def callbackHandler(access_token, expires):
    cherrypy.response.cookie[constants.FACEBOOK_ACCESS_TOKEN] = access_token
    if expires: cherrypy.response.cookie[constants.FACEBOOK_ACCESS_TOKEN]['expires'] = expires



