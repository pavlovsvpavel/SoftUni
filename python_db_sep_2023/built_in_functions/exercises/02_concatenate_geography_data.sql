CREATE VIEW view_continents_countries_currencies_details
AS
SELECT
    CONCAT(TRIM(con.continent_name), ': ', con.continent_code)
        AS "Continent Details",
    CONCAT_WS(' - ', coun.country_name, coun.capital, coun.area_in_sq_km, 'km2')
        AS "Country Information",
    CONCAT(cur.description, ' (', cur.currency_code, ')')
        AS "Currencies"
FROM
    countries AS coun

JOIN continents AS con ON coun.continent_code = con.continent_code
JOIN currencies AS cur ON coun.currency_code = cur.currency_code

ORDER BY
    coun.country_name,
    cur.description;
