import base

class todo(base.base):
    def add(self, userid, name):
        inserttodo = "select addtodo(%s, %s);" 
        self.cur.execute(inserttodo, (name, userid))
        self.conn.commit()
    
    def insertbefore(self, todoid, beforeid):
        pass
    
    def setdonestatus(self, todoid):
        setdone = "update todo set status_id = 1 where id_todo = %s;" 
        self.cur.execute(setdone, (todoid,))
        self.conn.commit()