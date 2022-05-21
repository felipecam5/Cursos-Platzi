/* 1. Función de Conteo */

CREATE OR REPLACE FUNCTION count_total_movies()
RETURNS int
LANGUAGE plpgsql
AS $$
BEGIN
	RETURN COUNT(*) FROM peliculas;
END
$$;

SELECT count_total_movies(); /* LLama la funcion*/

/* 
    1. Esta vez, retorna un entero con "RETUNS int"
    2. Se utiliza la sentencia "RETURN" en la fila 8.
    3. No va a crear nada, solo retorna el valor total de peliculas.
*/

/* 2.1 Funcion Trigger
        1. Esta es una funcion especial destinada a ser ejecutada cuando se cumpla una condicion o procedimiento previo
*/

CREATE OR REPLACE FUNCTION duplicate_records()
RETURNS trigger
LANGUAGE plpgsql
AS $$
BEGIN
	INSERT INTO aaab(bbba,ccca)
	VALUES (NEW.bbb, NEW.ccc);
	RETURN NEW;
END
$$;

/*
    1. Las funciones de trigger siempre retornan: "RETURNS trigger"
    2. De igual forma, siempre trabajan con un parametro "NEW", el cual proviene del TRIGGER en sí (Ver 2.2 (Siguiente))
    3. Basicamente, la funcion inserta los valores de bbb,ccc de la tabla NEW, en la tabla aaab.
*/

/* 2.2 TRIGGER en sí */
CREATE TRIGGER aaa_changes
	BEFORE INSERT
	ON aaa
	FOR EACH ROW
	EXECUTE PROCEDURE duplicate_records();

 /*
    1. Utiliza la palabra reservada "TRIGGER" en la sentencia de CREATE
    2. Traduce en que, ejecute la funcion trigger para cada row, antes de que se inserte información en la tabla aaa.
  */   


/* 3. Cuando se dispara */
INSERT INTO aaa(bbb,ccc)
VALUES ('abcde', 'efghi');
