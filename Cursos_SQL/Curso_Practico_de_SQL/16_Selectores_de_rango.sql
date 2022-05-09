SELECT int4range(10,20) @>19;

SELECT numrange(11.1,22.2) && numrange(20.0, 30.0)

SELECT UPPER (int8range(15,25));

SELECT LOWER (int8range(15,25));

SELECT int4range(10,20) * int4range(15,25)

SELECT ISEMPTY (numrange(10,24))

SELECT *
FROM platzi.alumnos
WHERE int4range(10,20) @>id

/* Reto: Interseccion de dos rangos con id_tutores y _id_carreras*/

SELECT *
FROM platzi.alumnos
WHERE alumnos.tutor_id<@(
	SELECT (int4range(MIN(tutor_id),MAX(tutor_id)) * int4range(MIN(carrera_id),MAX(carrera_id))) AS valores_comunes
	FROM platzi.alumnos
)

SELECT numrange(
    (SELECT MIN (tutor_id) from platzi.alumnos),
    (SELECT MAX (tutor_id) from platzi.alumnos)
) * numrange(
    (SELECT MIN (carrera_id) from platzi.alumnos),
    (SELECT MAX (carrera_id) from platzi.alumnos)

);
