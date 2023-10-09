SELECT
    CONCAT_WS(' ', c.first_name, c.last_name) AS full_name,
    c.email,
    MAX(b.rating) AS rating
FROM
    creators AS c
INNER JOIN
    creators_board_games AS cb
    ON
    c.id = cb.creator_id
INNER JOIN
    board_games AS b
    ON
    cb.board_game_id = b.id
WHERE
    c.email LIKE '%.com'
GROUP BY
    full_name,
    c.email
ORDER BY
    full_name
;