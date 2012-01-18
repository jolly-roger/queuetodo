import cherrypy
import os.path
import psycopg2
from http.cookies import SimpleCookie
import constants
import mainmenu


class queuetodo(object):
    @cherrypy.expose
    def index(self):
        return '''<html>
            <head>
            </head>
            <body>''' \
                + mainmenu.get(cherrypy.request) + \
                '''</body>
        </html>'''
    
    @cherrypy.expose
    def addtodo(self, todoname=None):        
        if not todoname == None:
            conn = psycopg2.connect(constants.DB_CONNECTION)
            cur = conn.cursor()
            cur.execute("insert into todo (name) values ('" + todoname + "');")
            conn.commit()
            cur.close()
            conn.close()
        
        return '''<html>
            <head>
            </head>
            <body>''' \
                + mainmenu.get(cherrypy.request) + \
                '''<form action="/addtodo" method="post">
                    <input type="text" name="todoname"/>
                    <input type="submit" value="Add"/>
                </form>
            </body>
        </html>'''
    
    @cherrypy.expose
    def listtodo(self):
        conn = psycopg2.connect(constants.DB_CONNECTION)
        cur = conn.cursor()
        cur.execute("select * from todo;")
        todos = cur.fetchall()
        todoslayout = ""
        
        for todo in todos:
            todoslayout += "<tr><td>" + todo[1] + "</td></tr>"
        
        return '''<html>
            <head>
            </head>
            <body>''' \
                + mainmenu.get(cherrypy.request) + \
                '''<table>''' \
                + todoslayout + \
                '''</table>
            </body>
        </html>'''
        
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