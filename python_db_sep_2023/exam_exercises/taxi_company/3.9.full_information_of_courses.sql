SELECT
    ad.name AS address,
    CASE
        WHEN EXTRACT('hour' FROM c.start) BETWEEN 6 AND 20 THEN 'Day'
        ELSE 'Night'
    END AS day_time,
    c.bill,
    cl.full_name,
    ca.make,
    ca.model,
    cat.name
FROM
    courses AS c
INNER JOIN
    addresses AS ad
    ON
    ad.id = c.from_address_id
INNER JOIN
    cars AS ca
    ON
    ca.id = c.car_id
INNER JOIN
    categories AS cat
    ON
    cat.id = ca.category_id
INNER JOIN
    clients AS cl
    ON
 cl.id = c.client_id
ORDER BY
    c.id
;
