CREATE OR REPLACE FUNCTION getsharedwithmetodos(userid bigint)
returns setof todo_status
AS
$BODY$
BEGIN
    return query select t.id_todo, t.name, t.status_id, s.name as status_name, t.is_shared
        from todo as t
        inner join status as s
            on t.status_id = s.id_status
        inner join todo_user as tu
            on t.id_todo = tu.todo_id and tu.is_owner = false
        inner join "user" as u
            on tu.user_id = u.id_user and u.facebook_user_id = userid
        where t.status_id <> 2;
END;
$BODY$
  LANGUAGE plpgsql;