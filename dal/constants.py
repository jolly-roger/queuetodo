DB_CONNECTION = 'dbname=queuetodo user=queuetodo password=6@,^K&=o'

GET_MY_TODOS = "select * from getmytodos(%s);"
GET_SHARED_WITH_ME_TODOS = "select * from getsharedwithmetodos(%s);"
GET_SHARED_TODOS = "select * from getsharedtodos(%s);"
GET_USER_TODOS = "select * from getusertodos(%s, %s);"

ADD_TODO = "select addtodo(%s, %s);"
SHARE_TODO = "select sharetodo(%s, %s);"
SET_DONE_STATUS = "update todo set status_id = 1 where id_todo = %s;"