DB_CONNECTION = 'dbname=queuetodo user=queuetodo password=6@,^K&=o'

GET_TODOS = "select * from gettodos(%(userid)s, %(statusid)s, %(isowner)s, %(excludestatus)s, %(isshared)s, %(excludeisshared)s);"

ADD_TODO = "select addtodo(%(todoname)s, %(userid)s);"
SHARE_TODO = "select sharetodo(%(todoid)s, %(friendid)s);"
SET_STATUS = "select setstatus(%(todoid)s, %(statusid)s);"
SET_DONE_STATUS = "update todo set status_id = 1 where id_todo = %(todoid)s;"

GET_ALL_STATUSES = "select * from status;"