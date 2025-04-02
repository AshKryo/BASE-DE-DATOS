Ejercicio 1

SHOW CHARACTER SET LIKE '%utf%';

Ejercicio 2

SHOW COLLATION WHERE Charset = 'latin1';

SHOW COLLATION WHERE Charset= 'latin1' ANDDefault = 'Yes';

Ejercicio 3

SHOW COLLATION WHERE Charset = 'utf8mb4' AND Collation LIKE '%_as%';

SHOW COLLATION WHERE Charset = 'utf8mb4' AND Collation LIKE '%_cs%';

Ejercicio 4

SELECT 'ó' = 'o' COLLATE utf8mb4_0900_ai_ci AS Result;

SELECT 'ó' != 'o' COLLATE utf8mb4_0900_as_ci AS Result;

Ejercicio 5

SELECT 'ñ' = 'n' COLLATE utf8mb4_spanish_ci AS Spanish_CI_Result