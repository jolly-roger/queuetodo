import cherrypy
import os.path
from http.cookies import SimpleCookie
import constants
import dal
import layout


class queuetodo(object):
    @cherrypy.expose
    def index(self):
        return layout.getIndex()
    
    @cherrypy.expose
    def addtodo(self, todoname=None):        
        if not todoname == None:
            dal.addtodo(todoname)
        
        return layout.getAddTodo()
    
    @cherrypy.expose
    def listtodo(self):
        todos = dal.getlisttodo()
        
        return layout.getListTodo(todos)
        
    @cherrypy.expose
    def logout(self):
        cherrypy.response.cookie[constants.FACEBOOK_CODE] = cherrypy.request.cookie[constants.FACEBOOK_CODE]
        cherrypy.response.cookie[constants.FACEBOOK_CODE]['expires'] = 0
        
        raise cherrypy.HTTPRedirect("/")
    
    @cherrypy.expose
    def signin(self):
        raise cherrypy.HTTPRedirect("https://www.facebook.com/dialog/oauth?" \
            "client_id=280195528701051&redirect_uri=http://dns-dig.net/signined")
        
        
    #https://graph.facebook.com/oauth/access_token?
    # client_id=YOUR_APP_ID&redirect_uri=YOUR_URL&
    # client_secret=YOUR_APP_SECRET&code=THE_CODE_FROM_ABOVE        
        
    @cherrypy.expose
    def signined(self, code=None, error_reason=None, error=None):
        if code:
            cherrypy.response.cookie[constants.FACEBOOK_CODE] = code
            
        raise cherrypy.HTTPRedirect("/#welcome")
    

queuetodoconf = os.path.join(os.path.dirname(__file__), 'queuetodo.conf')

cherrypy.quickstart(queuetodo(), config=queuetodoconf)