SELECT
    user_id,
    TO_CHAR(AGE(starts_at, booked_at), 'MM "mons" DD "days" HH24:MI:SS') AS "Early Bids"
FROM
    bookings
WHERE
    starts_at - booked_at >= INTERVAL '10 months';
