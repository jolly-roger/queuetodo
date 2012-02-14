CREATE OR REPLACE FUNCTION addtodo(todo_name text, user_id integer) returns boolean AS
$BODY$
declare
    new_todo_id bigint;
BEGIN
    insert into todo (name) values (todo_name) returning id_todo into new_todo_id;
    insert into todo_user values (new_todo_id, user_id);
    
    return true;
END;
$BODY$
  LANGUAGE plpgsql;