SELECT
    population,
    LENGTH(CAST(population AS text)) AS "length"

FROM
    countries;
