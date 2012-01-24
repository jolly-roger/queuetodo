import cherrypy

from facebook import authorization


HEADER = "<!DOCTYPE html>" \
    "<html>" \
        "<head>" \
            "<script type=\"text/javascript\" src=\"/javascript\"></script>" \
            "<style>" \
                ".todo.over {" \
                    "border-top: 2px dashed #000;" \
                "}" \
                "* {margin: 0;}" \
                "html, body {height: 100%;}" \
                "#wrap {" \
                    "min-height: 100%;" \
                    "height: auto !important;" \
                    "height: 100%;" \
                    "margin: 0 auto -100px;" \
                "}" \
                "footer, .push {" \
                    "height: 100px;" \
                "}" \
                "footer {background: #B5C1C0;}" \
            "</style>" \
        "</head>" \
            "<body>" \
                "<div id=\"wrap\">"

FOOTER = "<div class=\"push\">" \
                "</div>" \
            "</div>" \
            "<footer>" \
                "<div id=\"donebasket\">Done basket</div>" \
            "</footer>"\
        "</body>" \
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
        todoslayout += "<div class=\"todo\" draggable=\"true\">" + todo[1] + "</div>"
    
    return  HEADER + getMainMenu() + todoslayout + FOOTER