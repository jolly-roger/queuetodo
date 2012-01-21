import cherrypy
import os.path
import dal
import layout

from facebook import authorization
from facebook import authentication
from facebook import user


class queuetodo(object):
    @cherrypy.expose
    def index(self):
        if not authorization.isAuthorized():
            return layout.getIndex()
        else:
            authorization.checkAuthorization()
        
            todos = dal.getlisttodo(user.getUserId())
        
            return layout.getListTodo(todos)
    
    @cherrypy.expose
    def addtodo(self, todoname=None):
        authorization.checkAuthorization()
        
        if not todoname == None:
            dal.addtodo(user.getUserId(), todoname)
        
        return layout.getAddTodo()        
        
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
    def authorizecallback(self, code=None, error_reason=None, error=None):
        if not authorization.isAuthorized():
            authorization.callbackHandler(code)
            authentication.authenticate(code)
            
            raise cherrypy.HTTPRedirect("/#welcome")
    

queuetodoconf = os.path.join(os.path.dirname(__file__), 'queuetodo.conf')

cherrypy.quickstart(queuetodo(), config=queuetodoconf)