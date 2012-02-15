import cherrypy
import os.path
import dal
import layout
import constants

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
        
            todos = dal.gettodos(user.getUserId(), 0)
        
            return layout.getInitTodos(todos)
            
    @cherrypy.expose
    def donelist(self):
        if not authorization.isAuthorized():
            return layout.getIndex()
        else:
            authorization.checkAuthorization()
        
            todos = dal.gettodos(user.getUserId(), 1)
        
            return layout.getDoneTodos(todos)
    
    @cherrypy.expose
    def addtodo(self, todoname=None):
        authorization.checkAuthorization()
        
        if not todoname == None:
            dal.addtodo(int(user.getUserId()), todoname)
        
        return layout.getAddTodo()
    
    @cherrypy.expose
    def comments(self, todoid):
        pass
    
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
            
    @cherrypy.expose
    def javascript(self):
        mochikit = open(constants.BASE_DIR + "javascript/mochikit/MochiKit.js").read()
        consts= open(constants.BASE_DIR + "javascript/constants.js").read()
        dnd = open(constants.BASE_DIR + "javascript/dnd.js").read()
        js = mochikit + consts + dnd
        
        return js
    
    @cherrypy.expose
    def insertbefore(self, todoid, beforeid):
        pass
    
    @cherrypy.expose
    def setdone(self, todoid=None):
        if not todoid == None:
            dal.setdonestatus(int(todoid))


queuetodoconf = os.path.join(os.path.dirname(__file__), 'queuetodo.conf')

cherrypy.quickstart(queuetodo(), config=queuetodoconf)