import cherrypy

from facebook import authorization


HEADER = "<!DOCTYPE html>" \
    "<html>" \
        "<head>" \
        "</head>" \
            "<body>" 

FOOTER = "</body>" \
    "</html>"

def getMainMenu():
    if authorization.isAuthorized():
        return "&nbsp;<a href=\"/\">home</a>" \
            "&nbsp;<a href=\"/addtodo\">add todo</a>" \
            "&nbsp;<a href=\"/logout\">logout</a>"
    else:
        return "&nbsp;<a href=\"/signin\">signin</a>"
    
def getIndex():
    return HEADER \
                + getMainMenu() + \
        FOOTER
        
def getAddTodo():
    return HEADER \
                + getMainMenu() + \
                '''<form action="/addtodo" method="post">
                    <input type="text" name="todoname"/>
                    <input type="submit" value="Add"/>
                </form>''' + \
        FOOTER
        
def getListTodo(todos):
    todoslayout = ""
        
    for todo in todos:
        todoslayout += "<div>" + todo[1] + "</div>"
    
    return  HEADER + getMainMenu() + todoslayout + FOOTER