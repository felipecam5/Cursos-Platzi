SELECT *
FROM platzi.alumnos
WHERE EXTRACT(YEAR FROM fecha_incorporacion) =2018;

SELECT *
FROM platzi.alumnos
WHERE DATE_PART ('YEAR', fecha_incorporacion) =2018;

SELECT *
FROM (
	SELECT *
	FROM platzi.alumnos
) AS fecha
WHERE DATE_PART('YEAR', fecha_incorporacion) =2020;

/* RETO: Que estudidantes empezaron en mayo de 2018*/
SELECT *
FROM platzi.alumnos
WHERE 
DATE_PART ('YEAR', fecha_incorporacion)=2018 AND
DATE_PART ('MONTH', fecha_incorporacion) = 5;

SELECT *
FROM platzi.alumnos
WHERE DATE_PART('YEAR', fecha_incorporacion) < (
	SELECT EXTRACT (YEAR from fecha_incorporacion)
	FROM platzi.alumnos
	WHERE tutor_id=20
	ORDER by fecha_incorporacion DESC
	LIMIT 1
);

SELECT *
FROM (
	SELECT *,
	DATE_PART('YEAR', fecha_incorporacion) AS anio_incorporacion,
	DATE_PART('MONTH', fecha_incorporacion) AS mes_incorporacion
	FROM platzi.alumnos
) AS fecha
WHERE anio_incorporacion =2020 AND mes_incorporacion =5;