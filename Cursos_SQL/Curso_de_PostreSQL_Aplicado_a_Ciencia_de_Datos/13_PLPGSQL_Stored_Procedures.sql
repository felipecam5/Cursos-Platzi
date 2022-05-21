/* Ejemplo de una sentencia de un Stored Procedures*/
CREATE OR REPLACE PROCEDURE test_drpcreate_procedure()
LANGUAGE SQL
AS $$
	DROP TABLE IF EXISTS aaa;
	CREATE TABLE aaa (bbb char(5) CONSTRAINT firstkey PRIMARY KEY)
$$;

CALL test_drpcreate_procedure(); /* Sentencia para llamar el procedimiento*/

/*
    1. La Palabra "PROCEDURE" es reservada.
    2. El lenguaje será SQL para sentecias y PLPGSQL para funciones
    3. Dento de $$.....$$ se encapsula el codigo a ser run.
    4. Despues de creado/corrido el procedimiento, aparecerá en el catalogo de procedimientos
*/

/* Ejemplo de una función*/

CREATE OR REPLACE FUNCTION test_dropcreate_function()
RETURNS VOID
LANGUAGE plpgsql
AS $$
BEGIN
	DROP TABLE IF EXISTS aaa;
	CREATE TABLE aaa (bbb char(5) CONSTRAINT firstkey PRIMARY KEY, ccc char(5));
	DROP TABLE IF EXISTS aaab;
	CREATE TABLE aaab (bbba char(5) CONSTRAINT secondkey PRIMARY KEY, ccca char(5));
END
$$;	

SELECT test_dropcreate_function(); /* Sentencia para llamar la funcion */

/* 
    1. Se usa la palabra reservada "FUNCTION"
    2. Requiere de la palabra reservada "RETURNS". En este caso, no retorna nada ("VOID"). 
    3. El lenguaje es "plpgsql"
    4. Ademas de tener "AS $$" y "$$", se debe tener un "BEGIN" y "END", donde se encapsula el codigo.
    5. Despues de creada/corrida la función, aparecerá en el catalogo de funciones.
*/