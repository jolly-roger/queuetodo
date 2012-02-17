from . import base
from . import constants

class todo(base.base):
    def __iadd__(self):
        base.base.__init__(self)    
    
    def add(self, userid, name):
        self.cur.execute(constants.ADD_TODO, (name, userid))
        self.conn.commit()
        
    def share(self, todoid, friendid):
        self.cur.execute(constants.SHARE_TODO, (todoid, friendid))
        self.conn.commit()
    
    def insertbefore(self, todoid, beforeid):
        pass
    
    def setdonestatus(self, todoid): 
        self.cur.execute(constants.SET_DONE_STATUS, (todoid,))
        self.conn.commit()