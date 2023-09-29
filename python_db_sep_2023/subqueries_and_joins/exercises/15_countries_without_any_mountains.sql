SELECT
    COUNT(*) AS countries_without_mountains
FROM
    countries
LEFT JOIN
    mountains_countries
    ON
    countries.country_code = mountains_countries.country_code
WHERE
    mountain_id IS NULL
;