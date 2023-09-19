SELECT
    (REGEXP_MATCHES("River Information", '([0-9]{4})', 'g'))[1] AS river_length
FROM
    view_river_info;


-- SELECT SUBSTRING("River Information" FROM '([0-9]{1,4})') AS "river_length"
-- FROM view_river_info;