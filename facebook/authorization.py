import cherrypy

from . import constants

    
def authorize():
    raise cherrypy.HTTPRedirect("https://www.facebook.com/dialog/oauth?" \
        "client_id=" + constants.APP_ID + "&redirect_uri=" + constants.CALLBACK_URL)
    
def callbackHandler(code):
    cherrypy.session[constants.FACEBOOK_CODE] = code
    
def isAuthorized():
    
    cherrypy.log.error(cherrypy.session.get(constants.FACEBOOK_CODE))
    
    return bool(cherrypy.session.get(constants.FACEBOOK_CODE))
    
def checkAuthorization():
    if not isAuthorized():
        raise cherrypy.HTTPRedirect("/")