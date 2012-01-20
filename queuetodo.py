import cherrypy
import os.path
import dal
import layout

from facebook import authorization
from facebook import authentication


class queuetodo(object):
    @cherrypy.expose
    def index(self):
        return layout.getIndex()
    
    @cherrypy.expose
    def addtodo(self, todoname=None):
        authorization.checkAuthorization()
        
        if not todoname == None:
            dal.addtodo(todoname)
        
        return layout.getAddTodo()
    
    @cherrypy.expose
    def listtodo(self):
        authorization.checkAuthorization()
        
        todos = dal.getlisttodo()
        
        return layout.getListTodo(todos)
        
    @cherrypy.expose
    def logout(self):
        authorization.checkAuthorization()
        authorization.deauthorize()
        authentication.deauthenticate()
        
        raise cherrypy.HTTPRedirect("/")
    
    @cherrypy.expose
    def signin(self):
        authorization.authorize();        

    @cherrypy.expose
    def authorizecallback(self, code=None, error_reason=None, error=None, access_token=None, expires=None):
        if not authorization.isAuthorized():
            authorization.callbackHandler(code)
            authentication.authenticate(code)
        
        if access_token:
            authentication.callbackHandler(access_token, expires)
            
            raise cherrypy.HTTPRedirect("/#welcome")
        
    @cherrypy.expose
    def authenticatecallback(self, access_token=None, expires=None):
        if access_token:
            authentication.callbackHandler(access_token, expires)
        
        raise cherrypy.HTTPRedirect("/#welcome")
    

queuetodoconf = os.path.join(os.path.dirname(__file__), 'queuetodo.conf')

cherrypy.quickstart(queuetodo(), config=queuetodoconf)