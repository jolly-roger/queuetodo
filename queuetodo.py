import cherrypy
import os.path
import dal
import layout
import constants

from isAuthorized import isAuthorized

from facebook import authorization
from facebook import authentication
from facebook import user


class queuetodo(object):
    @cherrypy.expose
    @isAuthorized
    def index(self):
        todos = dal.gettodos(user.getUserId(), 0)
    
        return layout.getInitTodos(todos)
            
    @cherrypy.expose
    @isAuthorized
    def donelist(self):
        todos = dal.gettodos(user.getUserId(), 1)
    
        return layout.getDoneTodos(todos)
    
    @cherrypy.expose
    @isAuthorized
    def addtodo(self, todoname=None):
        if not todoname == None:
            dal.addtodo(int(user.getUserId()), todoname)
    
        return layout.getAddTodo()
    
    @cherrypy.expose
    def comments(self, todoid):
        pass
    
    @cherrypy.expose
    def logout(self):
        authorization.checkAuthorization()
        user.unloadUser()
        
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
    @isAuthorized
    def setdone(self, todoid=None):
        if not todoid == None:
            dal.setdonestatus(int(todoid))


queuetodoconf = os.path.join(os.path.dirname(__file__), 'queuetodo.conf')

cherrypy.quickstart(queuetodo(), config=queuetodoconf)