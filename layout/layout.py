import cherrypy
import constants

from jinja2 import Environment, FileSystemLoader

from facebook import constants as facebookConstatns

env = Environment(loader = FileSystemLoader(constants.BASE_DIR + "layout/templates"))
env.globals["session"] = cherrypy.session
env.globals["facebookConstatns"] = facebookConstatns.IS_SIGNED_REQUEST


def getSignin():
    tmpl = env.get_template("pages/signin.html")
    return tmpl.render()

def getAddTodo():
    tmpl = env.get_template("pages/addTodo.html")
    return tmpl.render()
    
#def getMyTodos(todos, friends, statuses, statusid):
def getMyTodos(todos, statuses, statusid):
    tmpl = env.get_template("pages/home.html")    
    #return tmpl.render(todos = todos, friends = friends, statuses = statuses, statusid = statusid)
    return tmpl.render(todos = todos, statuses = statuses, statusid = statusid)
    
def getSharedWithMeTodos(todos):
    #return getTodoList(todos, None, "Shared With Me")
    #return getTodoList(todos, "Shared With Me")
    tmpl = env.get_template("pages/sharedWithMe.html")    
    return tmpl.render(title = "Shared WithMe", todos = todos)
    
def getSharedTodos(todos):
    #return getTodoList(todos, None, "Shared")
    #return getTodoList(todos, "Shared")
    tmpl = env.get_template("pages/shared.html")    
    return tmpl.render(title = "Shared", todos = todos)

#def getTodoList(todos, friends, title):
def getTodoList(todos, title):
    tmpl = env.get_template("todoList.html")    
    #return tmpl.render(title = title, todos = todos, friends = friends)
    return tmpl.render(title = title, todos = todos)