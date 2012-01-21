import constants
import psycopg2

def addtodo(userid, name):
    conn = psycopg2.connect(constants.DB_CONNECTION)
    cur = conn.cursor()
    cur.execute("insert into todo (name, user_id) values ('" + name + "', " + userid + ");")
    conn.commit()
    cur.close()
    conn.close()
    
def getlisttodo(userid):
    conn = psycopg2.connect(constants.DB_CONNECTION)
    cur = conn.cursor()
    cur.execute("select * from todo where user_id = " + userid + ";")
    todos = cur.fetchall()
    cur.close()
    conn.close()
    
    return todos