CREATE VIEW continent_currency_usage
AS
SELECT
    continent_code,
    currency_code,
    count_currencies AS "currency_usage"
FROM
    (SELECT
        continent_code,
        currency_code,
        COUNT(currency_code) AS count_currencies,
        DENSE_RANK () OVER (
        PARTITION BY continent_code
        ORDER BY COUNT(currency_code) DESC
        ) AS continent_rank
     FROM
         countries
    GROUP BY
        continent_code,
        currency_code
    HAVING
        COUNT(currency_code) > 1) AS result
WHERE
    continent_rank = 1
ORDER BY
    currency_usage DESC
;
