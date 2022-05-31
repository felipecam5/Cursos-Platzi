/* Iteración en SQL*/

WITH RECURSIVE tabla_recursiva(n) AS ( /* El "WITH" indica que es una Common Table Expression. Mientras que el "RECURSIVE" indica que es una iteración*/
    VALUES(1)
    UNION ALL
    SELECT n+1 FROM tabla_recursiva WHERE n < 100
) SELECT SUM(n) FROM tabla_recursiva;