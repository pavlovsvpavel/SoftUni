SELECT
    a.name AS "Animal Name",
    EXTRACT('Year' FROM a.birthdate) AS "Birth Year",
    at.animal_type
FROM animals AS a
INNER JOIN
    animal_types AS at
ON
    a.animal_type_id = at.id
WHERE
    a.owner_id IS NULL
    AND
    at.animal_type <> 'Birds'
    AND
    AGE('2022-01-01', a.birthdate) < interval '5 years'
ORDER BY
    a.name
;