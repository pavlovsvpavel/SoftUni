SELECT
    AVG(area_in_sq_km) AS min_average_area
FROM
    countries
GROUP BY
    continent_code
ORDER BY
    min_average_area
LIMIT 1
;