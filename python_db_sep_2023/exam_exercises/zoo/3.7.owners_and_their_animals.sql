SELECT
    o.name AS "Owner",
    COUNT(a.name) AS "Count of animals"
FROM
    owners AS o
INNER JOIN
    animals AS a
ON
    a.owner_id = o.id
GROUP BY
    o.name
ORDER BY
    "Count of animals" DESC,
    o.name
LIMIT 5
;