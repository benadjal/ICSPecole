CREATE OR REPLACE FUNCTION insert_eleve(
		
		IN nom 				VARCHAR(30),
		IN prenom 			VARCHAR(30),
		IN datenaissance 	DATE,
		IN lieunaissance 	VARCHAR(30),
		IN telephone 		INTEGER,
		IN email 			VARCHAR(30)
)
RETURNS VOID AS
$BODY$
DECLARE

BEGIN

insert into televe (id,nom, prenom, datenaissance, lieunaissance, telephone, email) VALUES (to_char(current_timestamp,'YYYYMMDDHHMISSMS'),nom, prenom, datenaissance, lieunaissance, telephone, email);


END;

$BODY$
LANGUAGE plpgsql;
