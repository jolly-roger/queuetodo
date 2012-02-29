create or replace function isshared(todoid bigint)
returns boolean
as
$body$
begin
    if (select true from todo_user where todo_id = todoid and is_owner = false limit 1) then
        return true;
    else
        return false;
    end if;
end;
$body$
language plpgsql;