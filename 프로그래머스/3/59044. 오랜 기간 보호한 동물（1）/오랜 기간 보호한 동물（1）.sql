# SELECT I.ANIMAL_ID AS 보호, O.ANIMAL_ID AS 입양 FROM ANIMAL_INS I
# LEFT OUTER JOIN ANIMAL_OUTS O
# ON I.ANIMAL_ID = O.ANIMAL_ID
# WHERE O.ANIMAL_ID IS NULL

SELECT I.NAME, I.DATETIME FROM ANIMAL_INS I
LEFT OUTER JOIN ANIMAL_OUTS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.ANIMAL_ID IS NULL
ORDER BY I.DATETIME
LIMIT 3