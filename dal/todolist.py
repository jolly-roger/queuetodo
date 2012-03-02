from . import base
from . import constants

class todoList(base.base):
    def __init__(self):
        base.base.__init__(self)
    
    def getmy(self, userid, statusid):
        self.cur.execute(constants.GET_TODOS, {"userid": userid, "statusid": statusid, "isowner": True,
            "excludestatus": False, "isshared": False, "excludeisshared": True})
        todos = self.cur.fetchall()
        
        return todos
    
    def getsharedwithme(self, userid):
        self.cur.execute(constants.GET_TODOS, {"userid": userid, "statusid": 2, "isowner": False, "excludestatus": True,
            "isshared": True, "excludeisshared": False})
        todos = self.cur.fetchall()
        
        return todos
    
    def getshared(self, userid):
        self.cur.execute(constants.GET_TODOS, {"userid": userid, "statusid": 2, "isowner": True, "excludestatus": True,
            "isshared": True, "excludeisshared": False})
        todos = self.cur.fetchall()
        
        return todos
        
    def get(self, userid, statusid):
        self.cur.execute(constants.GET_USER_TODOS, {"userid": userid, "statusid": statusid})
        todos = self.cur.fetchall()
        
        return todos