import cherrypy
import os.path
import psycopg2


class queuetodo(object):
    FACEBOOK_CODE = 'facebook_code'    
    
    @cherrypy.expose
    def index(self):
        menu = ""
        
        if len(cherrypy.request.cookie) > 0 and cherrypy.request.cookie[self.FACEBOOK_CODE]:
            menu += '&nbsp;<a href="/addtodo">add todo</a>' \
                '&nbsp;<a href="/listtodo">list todo</a>'
        
        return '''<html>
            <head>
            </head>
            <body>''' \
                + menu + \
                '''&nbsp;<a href="/signin">signin</a>
            </body>
        </html>'''
    
    @cherrypy.expose
    def addtodo(self, todoname=None):        
        if not todoname == None:
            conn = psycopg2.connect("dbname=queuetodo user=queuetodo password=6@,^K&=o")
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
        conn = psycopg2.connect("dbname=queuetodo user=queuetodo password=6@,^K&=o")
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
    def signup(self):
        pass
    
    @cherrypy.expose
    def signin(self):
        raise cherrypy.HTTPRedirect("https://www.facebook.com/dialog/oauth?" \
            "client_id=280195528701051&redirect_uri=http://dns-dig.net/signined", 303)
        
    @cherrypy.expose
    def signined(self, code=None, error_reason=None, error=None):
        if code:
            cherrypy.response.cookie[self.FACEBOOK_CODE] = code
            cherrypy.response.cookie[self.FACEBOOK_CODE]['domain'] = 'dns-dig.net'
            cherrypy.response.cookie[self.FACEBOOK_CODE]['path'] = '/'
            
        raise cherrypy.HTTPRedirect("/", 303)
    

queuetodoconf = os.path.join(os.path.dirname(__file__), 'queuetodo.conf')

cherrypy.quickstart(queuetodo(), config=queuetodoconf)