SELECT nombre, apellido, email, fecha_incorporacion,
CASE
WHEN MIN(fecha_incorporacion) > CURRENT_TIMESTAMP THEN 'hay mas de 100'
WHEN MIN(fecha_incorporacion) > DATE('2018-09-04') THEN 'La antiguedad es menor a 4 años'
ELSE'La antiguedad es mayor a 4 años'
END AS texto
FROM platzi.alumnos
GROUP BY nombre, apellido, email, fecha_incorporacion;
