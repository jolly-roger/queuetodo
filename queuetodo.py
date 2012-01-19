import cherrypy
import os.path
import dal
import layout

from facebook import authorization


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
        authorization.logout()
        authorization.checkAuthorization()      
    
    @cherrypy.expose
    def signin(self):
        authorization.signin();        
        
    #https://graph.facebook.com/oauth/access_token?
    # client_id=YOUR_APP_ID&redirect_uri=YOUR_URL&
    # client_secret=YOUR_APP_SECRET&code=THE_CODE_FROM_ABOVE        
        
    @cherrypy.expose
    def signincallback(self, code=None, error_reason=None, error=None):
        if code:
            authorization.callbackHandler(code)
            
        raise cherrypy.HTTPRedirect("/#welcome")
    

queuetodoconf = os.path.join(os.path.dirname(__file__), 'queuetodo.conf')

cherrypy.quickstart(queuetodo(), config=queuetodoconf)