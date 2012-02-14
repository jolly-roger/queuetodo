CREATE OR REPLACE FUNCTION getusertodos(user_id bigint, status_id bigint) returns setof todo AS
$BODY$
BEGIN
    select * from todo as t where t.id_todo in (select tu.todo_id from todo_user as tu where tu.user_id = user_id) and
        t.status_id = status_id;
END;
$BODY$
  LANGUAGE plpgsql;