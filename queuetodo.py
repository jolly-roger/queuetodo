import cherrypy
import os.path
import psycopg2
from http.cookies import SimpleCookie


class queuetodo(object):
    FACEBOOK_CODE = 'facebook_code'
    DB_CONNECTION = 'dbname=queuetodo user=queuetodo password=6@,^K&=o'
    
    @cherrypy.expose
    def index(self):
        menu = ""
        
        if len(cherrypy.request.cookie) > 0 and cherrypy.request.cookie[self.FACEBOOK_CODE]:
            menu += '&nbsp;<a href="/addtodo">add todo</a>' \
                '&nbsp;<a href="/listtodo">list todo</a>' \
                '&nbsp;<a href="/logout">logout</a>'
        else:
            menu += '&nbsp;<a href="/signin">signin</a>' 
        
        return '''<html>
            <head>
            </head>
            <body>''' \
                + menu + \
                '''</body>
        </html>'''
    
    @cherrypy.expose
    def addtodo(self, todoname=None):        
        if not todoname == None:
            conn = psycopg2.connect(self.DB_CONNECTION)
            cur = conn.cursor()
            cur.execute("insert into todo (name) values ('" + todoname + "');")
            conn.commit()
            cur.close()
            conn.close()
        
        return '''<html>
            <head>
            </head>
            <body>
                <form action="/addtodo" method="post">
                    <input type="text" name="todoname"/>
                    <input type="submit" value="Add"/>
                </form>
            </body>
        </html>'''
    
    @cherrypy.expose
    def listtodo(self):
        conn = psycopg2.connect(self.DB_CONNECTION)
        cur = conn.cursor()
        cur.execute("select * from todo;")
        todos = cur.fetchall()
        todoslayout = ""
        
        for todo in todos:
            todoslayout += "<tr><td>" + todo[1] + "</td></tr>"
        
        return '''<html>
            <head>
            </head>
            <body>
                <table>''' \
                + todoslayout + \
                '''</table>
            </body>
        </html>'''
        
    @cherrypy.expose
    def logout(self):
        cherrypy.response.cookie[self.FACEBOOK_CODE] = cherrypy.request.cookie[self.FACEBOOK_CODE]
        #cherrypy.response.cookie[self.FACEBOOK_CODE]['domain'] = 'dns-dig.net'
        #cherrypy.response.cookie[self.FACEBOOK_CODE]['path'] = '/'
        cherrypy.response.cookie[self.FACEBOOK_CODE]['expires'] = 0
        
        raise cherrypy.HTTPRedirect("/", 303)
    
    @cherrypy.expose
    def signin(self):
        raise cherrypy.HTTPRedirect("https://www.facebook.com/dialog/oauth?" \
            "client_id=280195528701051&redirect_uri=http://dns-dig.net/signined", 303)
        
        
    #https://graph.facebook.com/oauth/access_token?
    # client_id=YOUR_APP_ID&redirect_uri=YOUR_URL&
    # client_secret=YOUR_APP_SECRET&code=THE_CODE_FROM_ABOVE        
        
    @cherrypy.expose
    def signined(self, code=None, error_reason=None, error=None):
        if code:
            cherrypy.response.cookie[self.FACEBOOK_CODE] = code
            #cherrypy.response.cookie[self.FACEBOOK_CODE]['domain'] = 'dns-dig.net'
            #cherrypy.response.cookie[self.FACEBOOK_CODE]['path'] = '/'
            
        raise cherrypy.InternalRedirect("/")
    

queuetodoconf = os.path.join(os.path.dirname(__file__), 'queuetodo.conf')

cherrypy.quickstart(queuetodo(), config=queuetodoconf)