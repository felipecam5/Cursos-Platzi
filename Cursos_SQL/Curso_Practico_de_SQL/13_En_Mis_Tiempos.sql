SELECT EXTRACT(YEAR FROM(fecha_incorporacion)) AS anio_incorporacion, *
FROM platzi.alumnos;

SELECT DATE_PART('YEAR',fecha_incorporacion)
FROM platzi.alumnos;

SELECT DATE_PART('MONTH',fecha_incorporacion) AS MES,
DATE_PART('DAY',fecha_incorporacion) AS DIA,
DATE_PART('YEAR',fecha_incorporacion) AS ANIO
FROM platzi.alumnos;

/* Reto: Sacar los campos de la hora*/

SELECT DATE_PART('MONTH',fecha_incorporacion) AS MES,
DATE_PART('DAY',fecha_incorporacion) AS DIA,
DATE_PART('YEAR',fecha_incorporacion) AS ANIO,
DATE_PART('HOUR',fecha_incorporacion) AS HORA,
DATE_PART('MINUTES',fecha_incorporacion) AS MINUTOS,
DATE_PART('SECONDS',fecha_incorporacion) AS SEGUNDOS, fecha_incorporacion
FROM platzi.alumnos;