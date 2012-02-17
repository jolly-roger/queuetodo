CREATE OR REPLACE FUNCTION addtodo(todoname varchar(256), userid bigint) returns boolean AS
$BODY$
declare
    new_todo_id bigint;
    local_user_id bigint;
BEGIN
    insert into todo (name) values (todoname) returning id_todo into new_todo_id;
    insert into todo_user values (new_todo_id, (select * from getuserid(userid)));
    
    return true;
END;
$BODY$
  LANGUAGE plpgsql;