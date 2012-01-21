import cherrypy

from facebook import authorization


def getMainMenu():
    if authorization.isAuthorized():
        return '&nbsp;<a href="/home">home</a>' \
            '&nbsp;<a href="/addtodo">add todo</a>' \
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
                + getMainMenu() + \
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
                + getMainMenu() + \
                '''<table>''' \
                + todoslayout + \
                '''</table>
            </body>
        </html>'''