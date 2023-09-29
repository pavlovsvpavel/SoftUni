SELECT
    a.name AS "Name",
    a.country AS "Country",
    CAST(b.booked_at AS DATE) AS "Booked at"
FROM
    apartments AS a
LEFT JOIN
    bookings AS b
ON
    a.booking_id = b.booking_id
LIMIT 10
;
