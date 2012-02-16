from . import base

class todoList(base.base):
    def __iadd__(self):
        base.base.__init__(self)
    
    def getmytodos(self, userid):
        getmytodos = "select * from getmytodos(%s);"
        self.cur.execute(getmytodos, (userid,))
        todos = self.cur.fetchall()
        
        return todos
    
    def getsharedwithmetodos(self, userid):
        getsharedwithmetodos = "select * from getsharedwithmetodos(%s);"
        self.cur.execute(getsharedwithmetodos, (userid,))
        todos = self.cur.fetchall()
        
        return todos
        
    def gettodos(self, userid, statusid):
        getusertodos = "select * from getusertodos(%s, %s);"
        self.cur.execute(getusertodos, (userid, statusid))
        todos = self.cur.fetchall()
        
        return todos