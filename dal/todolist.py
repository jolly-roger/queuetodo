from . import base
from . import constants

import dal.entities.todo


class todoList(base.base):
    def __init__(self):
        base.base.__init__(self)
    
    def getmy(self, userid, statusid):
        self.cur.execute(constants.GET_TODOS, {"userid": userid, "statusid": statusid, "isowner": True,
            "excludestatus": False, "isshared": False, "excludeisshared": True})
        rawtodos = self.cur.fetchall()
        
        return self._getTodoList(rawtodos)
    
    def getsharedwithme(self, userid):
        self.cur.execute(constants.GET_TODOS, {"userid": userid, "statusid": 2, "isowner": False, "excludestatus": True,
            "isshared": True, "excludeisshared": False})
        rawtodos = self.cur.fetchall()
        
        return self._getTodoList(rawtodos)
    
    def getshared(self, userid):
        self.cur.execute(constants.GET_TODOS, {"userid": userid, "statusid": 2, "isowner": True, "excludestatus": True,
            "isshared": True, "excludeisshared": False})
        rawtodos = self.cur.fetchall()
        
        return self._getTodoList(rawtodos)
    
    def _getTodoList(self, rawtodos):
        todos = []
        
        for rawtodo in rawtodos:
            todos[len(todos):] = [dal.entities.todo(rawtodo[0], rawtodo[1], rawtodo[2], rawtodo[3], rawtodo[4],
                rawtodo[5])]
            
        return todos