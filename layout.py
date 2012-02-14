import cherrypy

from facebook import authorization


INDEX_HEADER = "<!DOCTYPE html>" \
    "<html>" \
        "<head>" \
        "</head>" \
            "<body>" \

INDEX_FOOTER = "</body>" \
    "</html>"


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
                "#footer, .push {" \
                    "height: 100px;" \
                "}" \
                "#footer {" \
                    "background: #B5C1C0;" \
                    "padding: 10px;"\
                "}" \
                "#donebasket {"\
                    "height: 80px;"\
                    "width: 80px;"\
                    "background: #ffffff;"\
                "}" \
            "</style>" \
        "</head>" \
            "<body>" \
                "<div id=\"wrap\">"

FOOTER = "<div class=\"push\">" \
                "</div>" \
            "</div>" \
            "<div id=\"footer\">" \
                "<div id=\"donebasket\"><a href=\"/donelist\">Done basket</a></div>" \
            "</div>"\
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
    return INDEX_HEADER \
                + getMainMenu() + \
        INDEX_FOOTER
        
def getAddTodo():
    return HEADER \
                + getMainMenu() + \
                '''<form action="/addtodo" method="post">
                    <input type="text" name="todoname"/>
                    <input type="submit" value="Add"/>
                </form>''' + \
        FOOTER
        
def getInitTodos(todos):
    return getTodoList(todos, "Current")
    
def getDoneTodos(todos):
    return getTodoList(todos, "Done")

def getTodoList(todos, title):
    todoslayout = ""
        
    for todo in todos:
        todoslayout += "<div class=\"todo\" >" + \
            "<input type=\"hidden\" class=\"todoid\" value=\"" + str(todo[0]) + "\" />" + \
            todo[1] + "</div>"
    
    return  HEADER + \
        getMainMenu() + \
        "<h3>" + title + "</h3>" + \
        todoslayout + \
        FOOTER
    
    