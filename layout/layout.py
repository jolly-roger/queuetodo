import cherrypy

from facebook import authorization

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('layout/templates'))


#INDEX_HEADER = "<!DOCTYPE html>" \
#    "<html>" \
#        "<head>" \
#        "</head>" \
#            "<body>" \
#
#INDEX_FOOTER = "</body>" \
#    "</html>"
#
#
#HEADER = "<!DOCTYPE html>" \
#    "<html>" \
#        "<head>" \
#            "<script type=\"text/javascript\" src=\"/javascript\"></script>" \
#            "<link rel=\"stylesheet\" type=\"text/css\" href=\"/css\" />" \
#        "</head>" \
#            "<body>" \
#                "<div id=\"wrap\">"
#
#FOOTER = "<div class=\"push\">" \
#                "</div>" \
#            "</div>" \
#            "<div id=\"footer\">" \
#                "<div id=\"donebasket\"><a href=\"/donelist\">Done basket</a></div>" \
#            "</div>"\
#        "</body>" \
#    "</html>"

def getMainMenu():
    if authorization.isAuthorized():
        return "&nbsp;<a href=\"/\">home</a>" \
            "&nbsp;<a href=\"/addtodo\">add todo</a>" \
            "&nbsp;<a href=\"/shared\">shared</a>" \
            "&nbsp;<a href=\"/sharedwithme\">shared with me</a>" \
            "&nbsp;<a href=\"/logout\">logout</a>"
    else:
        return "&nbsp;<a href=\"/signin\">signin</a>"
    
def getIndex():
    tmpl = env.get_template('baseEmpty.html')
    
    return tmpl.render(content = getMainMenu())
    
    #return INDEX_HEADER \
    #            + getMainMenu() + \
    #    INDEX_FOOTER
        
def getAddTodo():
    tmpl = env.get_template('base.html')
    
    return tmpl.render(content = etMainMenu() + \
        '''<form action="/addtodo" method="post">
            <textarea rows=\"5\" cols=\"50\" name="todoname"></textarea>
            <input type="submit" value="Add"/>
        </form>''')
    
    
    #return HEADER \
    #            + getMainMenu() + \
    #            '''<form action="/addtodo" method="post">
    #                <textarea rows=\"5\" cols=\"50\" name="todoname"></textarea>
    #                <input type="submit" value="Add"/>
    #            </form>''' + \
    #    FOOTER
        
def getInitTodos(todos, friends):
    return getTodoList(todos, friends, "Current")
    
def getDoneTodos(todos):
    return getTodoList(todos, None, "Done")
    
def getSharedWithMeTodos(todos):
    return getTodoList(todos, None, "Shared With Me")
    
def getSharedTodos(todos):
    return getTodoList(todos, None, "Shared")

def getTodoList(todos, friends, title):
    todoslayout = ""
    friendslayout = ""
        
    for todo in todos:
        todoslayout += "<div class=\"todo\" >" + \
            "<input type=\"hidden\" class=\"todoid\" value=\"" + str(todo[0]) + "\" />" + \
            todo[1] + "</div>"
        
    if not friends == None:
        for friend in friends["data"]:
            friendslayout += "<div class=\"friend\" >" + \
                "<input type=\"hidden\" class=\"friendid\" value=\"" + friend["id"] + "\" />" + \
                friend["name"] + "</div>"
    
    tmpl = env.get_template('base.html')
    
    return tmpl.render(content = getMainMenu() + \
        "<table><tr><td valign=\"top\">" + \
        "<h3>" + title + "</h3>" + \
        todoslayout + \
        "</td><td>" + \
        friendslayout + \
        "</td></tr></table>")    
    
    #return  HEADER + \
    #    getMainMenu() + \
    #    "<table><tr><td valign=\"top\">" + \
    #    "<h3>" + title + "</h3>" + \
    #    todoslayout + \
    #    "</td><td>" + \
    #    friendslayout + \
    #    "</td></tr></table>" + \
    #    FOOTER
    

#import cherrypy

#
#class Root:
#    @cherrypy.expose
#    def index(self):
#        tmpl = env.get_template('index.html')
#        return tmpl.render(salutation='Hello', target='World')