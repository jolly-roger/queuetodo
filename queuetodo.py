import cherrypy
import os.path
import psycopg2


class queuetodo(object):
    @cherrypy.expose
    def index(self):
        return '''<html>
            <head>
            </head>
            <body>
                <a href="/addtodo">add todo</a>
                <a href="/listtodo">list todo</a>
                <a href="/signin">signin</a>
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
        return "Yo facebook!!!"
    

queuetodoconf = os.path.join(os.path.dirname(__file__), 'queuetodo.conf')

cherrypy.quickstart(queuetodo(), config=queuetodoconf)