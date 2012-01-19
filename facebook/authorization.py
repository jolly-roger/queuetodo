import cherrypy
import constants


FACEBOOK_CODE = 'facebook_code'
CALLBACK_URL = "http://dns-dig.net/signincallback"

def logout():
    cherrypy.response.cookie[FACEBOOK_CODE] = cherrypy.request.cookie[FACEBOOK_CODE]
    cherrypy.response.cookie[FACEBOOK_CODE]['expires'] = 0
    
def signin():
    raise cherrypy.HTTPRedirect("https://www.facebook.com/dialog/oauth?" \
        "client_id=" + constants.APP_ID + "&redirect_uri=" + CALLBACK_URL)
    
def callbackHandler(code):
    cherrypy.response.cookie[FACEBOOK_CODE] = code
    
def isAuthorized():
    return bool(len(cherrypy.request.cookie) > 0 and cherrypy.request.cookie[FACEBOOK_CODE])
    
def checkAuthorization():
    if not isAuthorized():
        raise cherrypy.HTTPRedirect("/")