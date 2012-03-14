import cherrypy

from facebook import authorization
from facebook import constants

from layout import layout


def isAuthorized(f):
    def _isAuthorized(*args, **kwargs):
        if cherrypy.session.get(constants.IS_SIGNED_REQUEST) is None:
            cherrypy.session[constants.IS_SIGNED_REQUEST] = False
            
            for kw in kwargs:
                if kw == constants.IS_SIGNED_REQUEST:
                    cherrypy.session[constants.IS_SIGNED_REQUEST] = True
                    break
        
        cherrypy.log.error(str(cherrypy.session.get(constants.IS_SIGNED_REQUEST)))
        
        if cherrypy.session.get(constants.IS_SIGNED_REQUEST):
            authorization.authorize();
            
            return f(*args, **kwargs)
        else:
            if not authorization.isAuthorized():
                return layout.getSignin()
            else:
                authorization.checkAuthorization()
                
                return f(*args, **kwargs)
            
    return _isAuthorized