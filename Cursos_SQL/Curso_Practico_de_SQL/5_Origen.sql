SELECT nombre, apellido, carrera
from platzi.alumnos as st
INNER JOIN platzi.carreras AS cr
ON st.carrera_id = cr.id;