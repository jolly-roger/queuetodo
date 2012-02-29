CREATE OR REPLACE FUNCTION getsharedwithmetodos(userid bigint)
returns setof todo_status
AS
$BODY$
BEGIN
    return query select t.id_todo, t.name, t.status_id, s.name as status_name, t.is_shared
        from todo as t
        inner join status as s
            on t.status_id = s.id_status
        where t.id_todo in (select tu.todo_id from todo_user as tu
            where tu.user_id = (select id_user from "user" where facebook_user_id = userid) and tu.is_owner = false) and
        t.status_id <> 2;
END;
$BODY$
  LANGUAGE plpgsql;