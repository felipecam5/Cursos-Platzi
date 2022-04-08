--1. Crear la tabla que se va a popular con la información resultante del trigger--
CREATE TABLE IF NOT EXISTS public.conteo_pasajero
(
    total integer,
    tiempo time with time zone,
    id integer NOT NULL DEFAULT nextval('conteo_pasajero_id_seq'::regclass),
    CONSTRAINT id_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.conteo_pasajero
    OWNER to postgres;

 --2.Modificar la PL para que retoner un triggeer y los valores nuevos--
 CREATE OR REPLACE FUNCTION public.importantepl3()
    RETURNS trigger
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE NOT LEAKPROOF
AS $BODY$
DECLARE
rec record := NULL;
contador integer :=0;
BEGIN
FOR rec IN SELECT * FROM pasajeros LOOP
	contador := contador +1;
	
END LOOP;
INSERT INTO conteo_pasajero (total, tiempo)
VALUES (contador, now());
RETURN NEW;
END
$BODY$;

ALTER FUNCTION public.importantepl3()
    OWNER TO postgres;   
--3. Crear el Trigger  
CREATE TRIGGER mitrigger
    AFTER INSERT
    ON public.pasajeros
    FOR EACH ROW
    EXECUTE FUNCTION public.importantepl3();  