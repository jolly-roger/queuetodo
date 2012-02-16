import cherrypy
import urllib.request

from . import constants


def getfriends():
    raw_access_data = str(urllib.request.urlopen("https://graph.facebook.com/me/friends?access_token=" +
        cherrypy.session.get(constants.FACEBOOK_ACCESS_TOKEN)).read(), encoding="utf-8")
    
    return raw_access_data