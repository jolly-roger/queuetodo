CREATE OR REPLACE FUNCTION getsharedwithmetodos(userid bigint) returns setof todo AS
$BODY$
BEGIN
    return query select * from todo as t
        where t.id_todo in (select tu.todo_id from todo_user as tu where tu.user_id = userid and tu.is_owner = false) and
        t.status_id = 0;
END;
$BODY$
  LANGUAGE plpgsql;