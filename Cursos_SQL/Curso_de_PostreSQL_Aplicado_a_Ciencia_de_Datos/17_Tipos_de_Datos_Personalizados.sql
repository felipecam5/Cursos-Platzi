/* Como crear tipos propias de valores (Como dominios en ArcGIS */

CREATE TYPE humor2 AS ENUM ('triste', 'normal', 'feliz'); /* Se utiliza la etiqueta "TYPE" y "ENUM". Esta ultima es una lista*/

CREATE TABLE persona_prueba2(
	nombre text,
	humor_actual humor
);

INSERT INTO persona_prueba2 VALUES ('Pablo', 'triste'); /* Los valores a ingresar quedaran restrigindos a los que pusimos al principio*/