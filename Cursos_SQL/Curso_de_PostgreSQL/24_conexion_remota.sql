--1. Crear o descargar dblink--

CREATE EXTENSION dblink;

--2. Hacer la conexion y descargar los datos--
SELECT * FROM pasajeros
INNER JOIN
dblink('dbname=remota
		port=5432
		host=127.0.0.1
		user=postgres
	    password=41778746Nh.',
	    'SELECT id,fecha FROM usuarios_vip')
		AS datos_remotos (id integer, fecha date)
on (pasajeros.id = datos_remotos.id);	