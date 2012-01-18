import cherrypy

class HelloWorld(object):
    def index(self, **args):
        return str(len(args))
    index.exposed = True

cherrypy.quickstart(HelloWorld())
