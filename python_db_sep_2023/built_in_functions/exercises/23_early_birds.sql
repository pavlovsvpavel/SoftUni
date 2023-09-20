SELECT
    user_id,
    TO_CHAR(AGE(starts_at, booked_at)) AS "Early Bids"
FROM
    bookings
WHERE
    starts_at - booked_at >= INTERVAL '10 months';
