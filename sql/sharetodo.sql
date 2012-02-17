CREATE OR REPLACE FUNCTION sharetodo(todoid bigint, friendid bigint) returns boolean AS
$BODY$
BEGIN
    insert into todo_user values (todoid, (select * from getuserid(friendid)), false);
    
    return true;
END;
$BODY$
  LANGUAGE plpgsql;