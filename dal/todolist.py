from . import base
from . import constants

class todoList(base.base):
    def __iadd__(self):
        base.base.__init__(self)
    
    def getmy(self, userid):
        self.cur.execute(constants.GET_MY_TODOS, {"userid": userid})
        todos = self.cur.fetchall()
        
        return todos
    
    def getsharedwithme(self, userid):
        self.cur.execute(constants.GET_SHARED_WITH_ME_TODOS, {"userid": userid})
        todos = self.cur.fetchall()
        
        return todos
    
    def getshared(self, userid):
        self.cur.execute(constants.GET_SHARED_TODOS, {"userid": userid})
        todos = self.cur.fetchall()
        
        return todos
        
    def get(self, userid, statusid):
        self.cur.execute(constants.GET_USER_TODOS, {"userid": userid, "statusid": statusid})
        todos = self.cur.fetchall()
        
        return todos