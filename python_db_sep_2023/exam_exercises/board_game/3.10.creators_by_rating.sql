SELECT
    c.last_name,
    CEIL(AVG(b.rating)) AS average_rating,
    p.name AS puplisher_name
FROM
    creators AS c
LEFT JOIN
    creators_board_games AS cb
    ON
    c.id = cb.creator_id
INNER JOIN
    board_games AS b
    ON
    cb.board_game_id = b.id
INNER JOIN
    publishers AS p
    ON
    b.publisher_id = p.id
WHERE
    p.name = 'Stonemaier Games'
GROUP BY
    c.last_name,
    p.name
ORDER BY
    average_rating DESC
;

