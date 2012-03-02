DB_CONNECTION = 'dbname=queuetodo user=queuetodo password=6@,^K&=o'

GET_TODOS = "select * from gettodos(%(userid)s, %(statusid)s, %(isowner)s, %(excludestatus)s, %(isshared)s, %(excludeisshared)s);"

ADD_TODO = "select addtodo(%(todoname)s, %(userid)s);"
SHARE_TODO = "select sharetodo(%(todoid)s, %(friendid)s);"
SET_STATUS = "select setstatus(%(todoid)s, %(statusid)s);"
SET_PRIORITY = "select setpriority(%(todoid)s, %(todopriority)s);"

GET_ALL_STATUSES = "select * from status;"