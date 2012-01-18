import constants
import psycopg2

def addtodo(name):
    conn = psycopg2.connect(constants.DB_CONNECTION)
    cur = conn.cursor()
    cur.execute("insert into todo (name) values ('" + name + "');")
    conn.commit()
    cur.close()
    conn.close()
    
def getlisttodo():
    conn = psycopg2.connect(constants.DB_CONNECTION)
    cur = conn.cursor()
    cur.execute("select * from todo;")
    todos = cur.fetchall()
    cur.close()
    conn.close()
    
    return todos