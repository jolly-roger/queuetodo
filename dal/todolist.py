from . import base
from . import constants

class todoList(base.base):
    def __init__(self):
        base.base.__init__(self)
    
    def getmy(self, userid, statusid):
        self.cur.execute(constants.GET_MY_TODOS, {"userid": userid, "statusid": statusid, "isowner": True})
        todos = self.cur.fetchall()
        
        return todos
    
    def getsharedwithme(self, userid):
        self.cur.execute(constants.GET_SHARED_WITH_ME_TODOS, {"userid": userid, "statusid": 2, "isowner": False})
        todos = self.cur.fetchall()
        
        return todos
    
    def getshared(self, userid):
        self.cur.execute(constants.GET_SHARED_TODOS, {"userid": userid, "statusid": 2, "isowner": True})
        todos = self.cur.fetchall()
        
        return todos
        
    def get(self, userid, statusid):
        self.cur.execute(constants.GET_USER_TODOS, {"userid": userid, "statusid": statusid})
        todos = self.cur.fetchall()
        
        return todos