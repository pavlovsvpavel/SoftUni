SELECT
    COUNT(c.id) AS countries_without_rivers
FROM
    countries AS c
LEFT JOIN countries_rivers AS cr
    ON c.country_code = cr.country_code
WHERE
    cr.river_id IS NULL;