CREATE OR REPLACE TABLE televe (
	id					INTEGER(12) PRIMARY KEY ,
    nom           	 	varchar(80),
    prenom           	varchar(80),           	
    datenaissance    	date,           		
    lieunaissance    	varchar(80),          	
    email            	varchar(80),
	telephone 			INTEGER
);