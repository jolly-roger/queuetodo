from . import base

class todo(base.base):
    def __iadd__(self):
        base.base.__init__(self)    
    
    def add(self, userid, name):
        addtodo = "select addtodo(%s, %s);" 
        self.cur.execute(addtodo, (name, userid))
        self.conn.commit()
        
    def share(self, todoid, friendid):
        sharetodo = "select sharetodo(%s, %s);" 
        self.cur.execute(sharetodo, (todoid, friendid))
        self.conn.commit()
    
    def insertbefore(self, todoid, beforeid):
        pass
    
    def setdonestatus(self, todoid):
        setdone = "update todo set status_id = 1 where id_todo = %s;" 
        self.cur.execute(setdone, (todoid,))
        self.conn.commit()