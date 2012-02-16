from . import base

class todoList(base.base):
    def __iadd__(self):
        base.base.__init__(self)
    
    def getmy(self, userid):
        getmytodos = "select * from getmytodos(%s);"
        self.cur.execute(getmytodos, (userid,))
        todos = self.cur.fetchall()
        
        return todos
    
    def getsharedwithme(self, userid):
        getsharedwithmetodos = "select * from getsharedwithmetodos(%s);"
        self.cur.execute(getsharedwithmetodos, (userid,))
        todos = self.cur.fetchall()
        
        return todos
    
    def getshared(self, userid):
        getsharedtodos = "select * from getsharedtodos(%s);"
        self.cur.execute(getsharedtodos, (userid,))
        todos = self.cur.fetchall()
        
        return todos
        
    def get(self, userid, statusid):
        getusertodos = "select * from getusertodos(%s, %s);"
        self.cur.execute(getusertodos, (userid, statusid))
        todos = self.cur.fetchall()
        
        return todos