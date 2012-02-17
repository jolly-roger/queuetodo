import cherrypy
import os.path
import layout
import constants

from isAuthorized import isAuthorized

from facebook import authorization
from facebook import authentication
from facebook import user
from facebook import friends

from dal import todo
from dal import todolist


class queuetodo(object):
    @cherrypy.expose
    @isAuthorized
    def index(self):
        tdl = todolist.todoList()
        todos = tdl.getmy(user.getUserId())
        tdl.close()
        frs = friends.getfriends()
    
        return layout.getInitTodos(todos, frs)
            
    @cherrypy.expose
    @isAuthorized
    def donelist(self):
        tdl = todolist.todoList()
        todos = tdl.get(user.getUserId(), 1)
        tdl.close()    
    
        return layout.getDoneTodos(todos)
        
    @cherrypy.expose
    @isAuthorized
    def sharedwithme(self):
        tdl = todolist.todoList()
        todos = tdl.getsharedwithme(user.getUserId())
        tdl.close()    
    
        return layout.getSharedWithMeTodos(todos)
        
    @cherrypy.expose
    @isAuthorized
    def shared(self):
        tdl = todolist.todoList()
        todos = tdl.getshared(user.getUserId())
        tdl.close()    
    
        return layout.getSharedTodos(todos)
    
    @cherrypy.expose
    @isAuthorized
    def addtodo(self, todoname=None):
        if not todoname == None:
            td = todo.todo()
            td.add(int(user.getUserId()), todoname)
            td.close()
    
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
        cherrypy.response.headers['Content-Type'] = "text/javascript"        
        
        mochikit = open(constants.BASE_DIR + "javascript/mochikit/MochiKit.js").read()
        consts= open(constants.BASE_DIR + "javascript/constants.js").read()
        dnd = open(constants.BASE_DIR + "javascript/dnd.js").read()
        js = mochikit + consts + dnd
        
        return js
    
    @cherrypy.expose
    def css(self):
        cherrypy.response.headers['Content-Type'] = "text/css"
        
        style = open(constants.BASE_DIR + "css/style.css").read()
        
        return style
    
    @cherrypy.expose
    def insertbefore(self, todoid, beforeid):
        pass
    
    @cherrypy.expose
    @isAuthorized
    def setdone(self, todoid=None):
        if not todoid == None:
            td = todo.todo()
            td.setdonestatus(int(todoid))
            td.close()
            
    @cherrypy.expose
    @isAuthorized
    def share(self, todoid, friendid):
        if not todoid == None and not friendid == None:
            td = todo.todo()
            td.share(int(todoid), int(friendid))
            td.close()


queuetodoconf = os.path.join(os.path.dirname(__file__), "queuetodo.conf")

cherrypy.quickstart(queuetodo(), config=queuetodoconf)