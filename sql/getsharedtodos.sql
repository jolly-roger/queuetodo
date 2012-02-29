CREATE OR REPLACE FUNCTION getsharedtodos(userid bigint)
returns setof todo_status
AS
$BODY$
BEGIN
    return query select t.id_todo, t.name, t.status_id, s.name as status_name,
            (select * from isshared(t.id_todo)) as is_shared
        from todo as t
        inner join status as s
            on t.status_id = s.id_status
        where t.id_todo in (
            select tu0.todo_id from todo_user as tu0
                inner join todo_user as tu1
                    on tu0.todo_id = tu1.todo_id
                where tu0.user_id = (select id_user from "user" where facebook_user_id = userid) and
                    tu0.is_owner = true and tu1.is_owner = false
        ) and t.status_id <> 2;
END;
$BODY$
  LANGUAGE plpgsql;