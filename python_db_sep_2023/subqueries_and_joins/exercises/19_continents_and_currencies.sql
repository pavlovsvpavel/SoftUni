CREATE VIEW continent_currency_usage
AS
SELECT
    continent_code,
    currency_code,
    COUNT(currency_code) AS "currency_usage",
    DENSE_RANK () OVER (
	PARTITION BY continent_code
	ORDER BY COUNT(currency_code) DESC
	) continent_rank

FROM
    countries
GROUP BY
    continent_code,
    currency_code
HAVING
    COUNT(continent_code) > 1
;
