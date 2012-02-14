import cherrypy
import os.path
import dal
import layout

from facebook import authorization
from facebook import authentication
from facebook import user


class queuetodo(object):
    @cherrypy.expose
    @cherrypy.tools.encode(encoding='utf-8')
    def index(self):
        cherrypy.response.headers['Content-Type'] = "text/html; charset=utf-8" 
        
        if not authorization.isAuthorized():
            return layout.getIndex()
        else:
            authorization.checkAuthorization()
        
            todos = dal.getlisttodos(user.getUserId())
        
            return layout.getListTodo(todos)
    
    @cherrypy.expose
    @cherrypy.tools.encode(encoding='utf-8')
    def addtodo(self, todoname=None):
        cherrypy.response.headers['Content-Type'] = "text/html; charset=utf-8" 
        
        authorization.checkAuthorization()
        
        if not todoname == None:
            dal.addtodo(user.getUserId(), todoname)
        
        return layout.getAddTodo()
    
    @cherrypy.expose
    @cherrypy.tools.encode(encoding='utf-8')
    def comments(self, todoid):
        pass
    
    @cherrypy.expose
    @cherrypy.tools.encode(encoding='utf-8')
    def logout(self):
        cherrypy.response.headers['Content-Type'] = "text/html; charset=utf-8" 
        
        authorization.checkAuthorization()
        authorization.deauthorize()
        authentication.deauthenticate()
        
        raise cherrypy.HTTPRedirect("/")
    
    @cherrypy.expose
    @cherrypy.tools.encode(encoding='utf-8')
    def signin(self):
        cherrypy.response.headers['Content-Type'] = "text/html; charset=utf-8" 
        
        authorization.authorize();        

    @cherrypy.expose
    @cherrypy.tools.encode(encoding='utf-8')
    def authorizecallback(self, code=None, error_reason=None, error=None):
        cherrypy.response.headers['Content-Type'] = "text/html; charset=utf-8" 
        
        if not authorization.isAuthorized():
            authorization.callbackHandler(code)
            authentication.authenticate(code)
            
            raise cherrypy.HTTPRedirect("/#welcome")
            
    @cherrypy.expose
    @cherrypy.tools.encode(encoding='utf-8')
    def javascript(self):
        mochikit = open("javascript/mochikit/MochiKit.js").read()
        constants = open("javascript/constants.js").read()
        dnd = open("javascript/dnd.js").read()
        js = mochikit + constants + dnd
        
        return js
    
    @cherrypy.expose
    @cherrypy.tools.encode(encoding='utf-8')
    def insertbefore(self, todoid, beforeid):
        pass
    
    @cherrypy.expose
    @cherrypy.tools.encode(encoding='utf-8')
    def setdone(self, todoid=None):
        if not todoid == None:
            dal.setdonestatus(int(todoid))


queuetodoconf = os.path.join(os.path.dirname(__file__), 'queuetodo.conf')

cherrypy.quickstart(queuetodo(), config=queuetodoconf)