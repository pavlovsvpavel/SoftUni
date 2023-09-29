SELECT
    m_c.country_code,
    COUNT(*) AS mountain_range_count
FROM
    mountains_countries AS m_c
INNER JOIN
    mountains AS m
ON
    m_c.mountain_id = m.id
WHERE
    m_c.country_code IN ('BG', 'RU', 'US')
GROUP BY
    m_c.country_code
ORDER BY
    mountain_range_count DESC
;
