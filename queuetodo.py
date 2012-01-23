import cherrypy
import os.path
import dal
import layout

from facebook import authorization
from facebook import authentication
from facebook import user


class queuetodo(object):
    @cherrypy.tools.encoding(encoding='utf-8') 
    @cherrypy.expose
    def index(self):
        cherrypy.response.headers['Content-Type'] = "text/html; charset=utf-8" 
        
        if not authorization.isAuthorized():
            return layout.getIndex()
        else:
            authorization.checkAuthorization()
        
            todos = dal.getlisttodos(user.getUserId())
        
            return layout.getListTodo(todos)
    
    @cherrypy.tools.encoding(encoding='utf-8') 
    @cherrypy.expose
    def addtodo(self, todoname=None):
        cherrypy.response.headers['Content-Type'] = "text/html; charset=utf-8" 
        
        authorization.checkAuthorization()
        
        if not todoname == None:
            dal.addtodo(user.getUserId(), todoname)
        
        return layout.getAddTodo()
    
    @cherrypy.tools.encoding(encoding='utf-8')     
    @cherrypy.expose
    def comments(self, todoid):
        pass
    
    @cherrypy.tools.encoding(encoding='utf-8')     
    @cherrypy.expose
    def logout(self):
        cherrypy.response.headers['Content-Type'] = "text/html; charset=utf-8" 
        
        authorization.checkAuthorization()
        authorization.deauthorize()
        authentication.deauthenticate()
        
        raise cherrypy.HTTPRedirect("/")
    
    @cherrypy.tools.encoding(encoding='utf-8') 
    @cherrypy.expose
    def signin(self):
        cherrypy.response.headers['Content-Type'] = "text/html; charset=utf-8" 
        
        authorization.authorize();        

    @cherrypy.tools.encoding(encoding='utf-8') 
    @cherrypy.expose
    def authorizecallback(self, code=None, error_reason=None, error=None):
        cherrypy.response.headers['Content-Type'] = "text/html; charset=utf-8" 
        
        if not authorization.isAuthorized():
            authorization.callbackHandler(code)
            authentication.authenticate(code)
            
            raise cherrypy.HTTPRedirect("/#welcome")
    

queuetodoconf = os.path.join(os.path.dirname(__file__), 'queuetodo.conf')

cherrypy.quickstart(queuetodo(), config=queuetodoconf)