CREATE OR REPLACE FUNCTION setstatus(todoid bigint, statusid bigint) returns boolean AS
$BODY$
BEGIN
    update todo set status_id = statusid, priority = 0 where id_todo = todoid;

    return true;
END;
$BODY$
  LANGUAGE plpgsql;