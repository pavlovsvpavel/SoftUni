SELECT
    COUNT(*) AS countries_without_mountains
FROM
    countries AS c
LEFT JOIN
    mountains_countries AS mc
    ON
    c.country_code = mc.country_code
WHERE
    mountain_id IS NULL
;