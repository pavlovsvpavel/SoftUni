SELECT
    CONCAT_WS(' - ', o.name, a.name) AS "Owners - Animals",
    o.phone_number AS "Phone Number",
    ac.cage_id AS "Cage ID"
FROM
    owners AS o
INNER JOIN
    animals AS a
ON
    a.owner_id = o.id
INNER JOIN
    animals_cages AS ac
ON
    ac.animal_id = a.id
WHERE
    a.animal_type_id = (
        SELECT
            at.id
        FROM
            animal_types AS at
        WHERE
            at.animal_type = 'Mammals'
        )
ORDER BY
    o.name,
    a.name DESC
;