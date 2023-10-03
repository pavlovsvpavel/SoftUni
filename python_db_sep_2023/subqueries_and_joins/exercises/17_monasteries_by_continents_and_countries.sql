UPDATE countries
SET country_name = 'Burma'
WHERE country_name = 'Myanmar'
;

INSERT INTO monasteries(monastery_name, country_code)
VALUES
    ('Hanga Abbey',
     (SELECT
          country_code
      FROM
          countries
      WHERE
          country_name = 'Tanzania'
      )
    );

INSERT INTO monasteries(monastery_name, country_code)
VALUES
    ('Myin-Tin-Daik',
     (SELECT
        country_code
      FROM
        countries
      WHERE
        country_name = 'Myanmar'
      )
    );

SELECT
    con.continent_name AS "Continent Name",
    c.country_name AS "Country Name",
    COUNT(m.*) AS "Monasteries Count"
FROM
    countries as c
INNER JOIN
    continents AS con
USING (continent_code)
LEFT JOIN
    monasteries AS m
USING (country_code)
WHERE
    c.three_rivers = False
GROUP BY
    c.country_name,
    con.continent_name
ORDER BY
    "Monasteries Count" DESC,
    "Country Name";
