create or replace type todo_status as (
    id_todo integer,
    name varchar(256),
    status_id integer,
    status_name varchar(50),
    is_shared boolean
);


CREATE OR REPLACE FUNCTION getmytodos(userid bigint, statusid bigint)
returns setof todo_status
AS
$BODY$
BEGIN
    return query select t.id_todo, t.name, t.status_id, s.name as status_name,
            (select * from isshared(t.id_todo)) as is_shared
        from todo as t
        inner join status as s
            on t.status_id = s.id_status
        where t.id_todo in (select tu.todo_id from todo_user as tu
            where tu.user_id = (select id_user from "user" where facebook_user_id = userid) and tu.is_owner = true) and
                t.status_id = statusid;
END;
$BODY$
  LANGUAGE plpgsql;