from . import base
from . import constants

class status(base.base):
    def __init__(self):
        base.base.__init__(self)    
    
    def getall(self):
        self.cur.execute(constants.GET_ALL_STATUSES)
        statuses = self.cur.fetchall()
        
        return statuses