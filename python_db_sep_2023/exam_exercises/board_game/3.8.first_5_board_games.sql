SELECT
    b.name,
    b.rating,
    c.name
FROM
    board_games AS b
INNER JOIN
    categories AS c
    ON
    b.category_id = c.id
INNER JOIN
    players_ranges AS p
    ON
    p.id = b.players_range_id
WHERE
    ((b.rating > 7.00
    AND
    b.name ILIKE '%a%')
    OR
    (b.rating > 7.50))
    AND
    (p.min_players >= 2 AND p.max_players <= 5)
ORDER BY
    b.name,
    b.rating DESC
LIMIT 5;