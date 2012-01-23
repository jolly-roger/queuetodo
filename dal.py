import constants
import psycopg2

def addtodo(userid, name):
    conn = psycopg2.connect(constants.DB_CONNECTION)
    cur = conn.cursor()
    inserttodo = "insert into todo (name, user_id) values (%s, %s);" 
    cur.execute(inserttodo, (name, userid))
    conn.commit()
    cur.close()
    conn.close()
    
def getlisttodos(userid):
    conn = psycopg2.connect(constants.DB_CONNECTION)
    cur = conn.cursor()
    selecttodos = "select * from todo where user_id = %s;"
    cur.execute(selecttodos, (userid,))
    todos = cur.fetchall()
    cur.close()
    conn.close()
    
    return todos

#def addcomment(todoid, name):
#    conn = psycopg2.connect(constants.DB_CONNECTION)
#    cur = conn.cursor()
#    cur.execute("insert into comments (todo_id, name) values ('" + todoid + "', " + name + ");")
#    conn.commit()
#    cur.close()
#    conn.close()
#    
#def getlistcomments(todoid):
#    conn = psycopg2.connect(constants.DB_CONNECTION)
#    cur = conn.cursor()
#    cur.execute("select * from comments where todo_id = " + todoid + ";")
#    comments = cur.fetchall()
#    cur.close()
#    conn.close()
#    
#    return comments