SELECT
    title,
    TRUNC(cost, 3) AS mofified_price
FROM
    books
ORDER BY id;
