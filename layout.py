import constants
import cherrypy


def getMainMenu():
    if len(cherrypy.request.cookie) > 0 and cherrypy.request.cookie[constants.FACEBOOK_CODE]:
        return '&nbsp;<a href="/addtodo">add todo</a>' \
            '&nbsp;<a href="/listtodo">list todo</a>' \
            '&nbsp;<a href="/logout">logout</a>'
    else:
        return '&nbsp;<a href="/signin">signin</a>'
    
def getIndex():
    return '''<html>
            <head>
            </head>
            <body>''' \
                + getMainMenu() + \
                '''</body>
        </html>'''
        
def getAddTodo():
    return '''<html>
            <head>
            </head>
            <body>''' \
                + mainmenu.get() + \
                '''<form action="/addtodo" method="post">
                    <input type="text" name="todoname"/>
                    <input type="submit" value="Add"/>
                </form>
            </body>
        </html>'''
        
def getListTodo(todos):
    todoslayout = ""
        
    for todo in todos:
        todoslayout += "<tr><td>" + todo[1] + "</td></tr>"
    
    return '''<html>
            <head>
            </head>
            <body>''' \
                + mainmenu.get() + \
                '''<table>''' \
                + todoslayout + \
                '''</table>
            </body>
        </html>'''