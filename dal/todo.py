from . import base
from . import constants

class todo(base.base):
    def __init__(self):
        base.base.__init__(self)    
    
    def add(self, userid, name):
        self.cur.execute(constants.ADD_TODO, {"todoname": name, "userid": userid})
        self.conn.commit()
        
    def share(self, todoid, friendid):
        self.cur.execute(constants.SHARE_TODO, {"todoid": todoid, "friendid": friendid})
        self.conn.commit()
    
    def insertbefore(self, todoid, beforeid):
        pass
    
    def setdonestatus(self, todoid): 
        self.cur.execute(constants.SET_DONE_STATUS, {"todoid": todoid})
        self.conn.commit()