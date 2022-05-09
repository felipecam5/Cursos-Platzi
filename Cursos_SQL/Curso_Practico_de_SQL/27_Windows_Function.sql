SELECT *, AVG(colegiatura) OVER(PARTITION BY carrera_id)
FROM platzi.alumnos;

SELECT *, AVG(colegiatura) OVER() /* No tiene partición, me trae el promedio de toda la table*/
FROM platzi.alumnos;

SELECT *, SUM (colegiatura) OVER(ORDER BY colegiatura)
FROM platzi.alumnos;

SELECT *, SUM (colegiatura) OVER(PARTITION BY carrera_id ORDER BY colegiatura)
FROM platzi.alumnos;

SELECT *, RANK () OVER(PARTITION BY carrera_id ORDER BY colegiatura DESC)
FROM platzi.alumnos;

SELECT *, RANK () OVER(PARTITION BY carrera_id ORDER BY colegiatura DESC ) AS brand_rank
FROM platzi.alumnos
ORDER BY carrera_id, brand_rank;
