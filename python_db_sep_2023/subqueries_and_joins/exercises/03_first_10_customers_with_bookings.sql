SELECT
    b.booking_id AS "Booking ID",
    CAST(b.starts_at AS DATE) AS "Start Date",
    b.apartment_id AS "Apartment ID",
    CONCAT_WS(' ', c.first_name, c.last_name) AS "Customer Name"
FROM
    bookings AS b
RIGHT JOIN
    customers AS c
ON
    b.customer_id = c.customer_id
ORDER BY
    "Customer Name"
LIMIT 10
;