import cherrypy
import urllib.request
import json

from . import constants


USER_URL = "https://graph.facebook.com/me"


def getUserId():
    raw_user_data = str(urllib.request.urlopen(USER_URL + "?" \
        "access_token=" + cherrypy.request.cookie[constants.FACEBOOK_ACCESS_TOKEN] + \
        "&fields=id").read(), encoding="utf-8")
    
    user_data = json.loads(raw_user_data)
    
    cherrypy.response.cookie['facebook_user_id'] = user_data['id']