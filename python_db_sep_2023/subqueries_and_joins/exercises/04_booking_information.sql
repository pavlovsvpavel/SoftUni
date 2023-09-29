SELECT
    b.booking_id AS "Booking ID",
    a.name AS "Apartment Owner",
    a.apartment_id AS "Apartment ID",
    CONCAT_WS(' ', c.first_name, c.last_name) AS "Customer Name"
FROM
    bookings AS b
FULL JOIN
    apartments AS a
ON
    b.booking_id = a.booking_id
FULL JOIN
    customers AS c
ON
    b.customer_id = c.customer_id
ORDER BY
    "Booking ID",
    "Apartment Owner",
    "Customer Name"
;