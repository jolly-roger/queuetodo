DB_CONNECTION = 'dbname=queuetodo user=queuetodo password=6@,^K&=o'

GET_MY_TODOS = "select * from gettodos(%(userid)s, %(statusid)s, %(isowner)s);"
GET_SHARED_WITH_ME_TODOS = "select * from gettodos(%(userid)s, %(statusid)s, %(isowner)s);"
GET_SHARED_TODOS = "select * from gettodos(%(userid)s, %(statusid)s, %(isowner)s);"
GET_USER_TODOS = "select * from getusertodos(%(userid)s, %(statusid)s);"

ADD_TODO = "select addtodo(%(todoname)s, %(userid)s);"
SHARE_TODO = "select sharetodo(%(todoid)s, %(friendid)s);"
SET_STATUS = "select setstatus(%(todoid)s, %(statusid)s);"
SET_DONE_STATUS = "update todo set status_id = 1 where id_todo = %(todoid)s;"

GET_ALL_STATUSES = "select * from status;"