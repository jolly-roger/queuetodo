CREATE OR REPLACE FUNCTION getsharedtodos(userid bigint) returns setof todo AS
$BODY$
BEGIN
    return query select * from todo as t
        where t.id_todo in (
            select tu0.todo_id from todo_user as tu0
                inner join todo_user as tu1
                    on tu0.todo_id = tu1.todo_id
                where tu0.user_id = (select id_user from "user" where facebook_user_id = userid) and
                    tu0.is_owner = true and tu1.is_owner = false
        ) and t.status_id = 0;
END;
$BODY$
  LANGUAGE plpgsql;