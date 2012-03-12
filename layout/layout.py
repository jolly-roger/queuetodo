import cherrypy
import constants

from jinja2 import Environment, FileSystemLoader


env = Environment(loader = FileSystemLoader(constants.BASE_DIR + "layout/templates"))


def getSignin():
    tmpl = env.get_template("signin.html")
    return tmpl.render()

def getAddTodo():
    tmpl = env.get_template("addTodo.html")
    return tmpl.render()
    
#def getMyTodos(todos, friends, statuses, statusid):
def getMyTodos(todos, statuses, statusid):
    tmpl = env.get_template("todoList.html")    
    #return tmpl.render(todos = todos, friends = friends, statuses = statuses, statusid = statusid)
    return tmpl.render(todos = todos, statuses = statuses, statusid = statusid)
    
def getSharedWithMeTodos(todos):
    #return getTodoList(todos, None, "Shared With Me")
    return getTodoList(todos, "Shared With Me")
    
def getSharedTodos(todos):
    #return getTodoList(todos, None, "Shared")
    return getTodoList(todos, "Shared")

#def getTodoList(todos, friends, title):
def getTodoList(todos, title):
    tmpl = env.get_template("todoList.html")    
    #return tmpl.render(title = title, todos = todos, friends = friends)
    return tmpl.render(title = title, todos = todos)