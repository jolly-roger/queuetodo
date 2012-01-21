import cherrypy

from . import constants


def deauthorize():
    cherrypy.response.cookie[constants.FACEBOOK_CODE] = cherrypy.request.cookie[constants.FACEBOOK_CODE]
    cherrypy.response.cookie[constants.FACEBOOK_CODE]['expires'] = 0
    
def authorize():
    raise cherrypy.HTTPRedirect("https://www.facebook.com/dialog/oauth?" \
        "client_id=" + constants.APP_ID + "&redirect_uri=" + constants.CALLBACK_URL)
    
def callbackHandler(code):
    cherrypy.response.cookie[constants.FACEBOOK_CODE] = code
    
def isAuthorized():
    return bool(len(cherrypy.request.cookie) > 0 and cherrypy.request.cookie[constants.FACEBOOK_CODE])
    
def checkAuthorization():
    if not isAuthorized():
        raise cherrypy.HTTPRedirect("/")