SELECT
    c.id,
    CONCAT(c.first_name, ' ', c.last_name) AS creator_name,
    c.email
FROM
    creators AS c
LEFT JOIN
    creators_board_games AS cb
    ON
    c.id = cb.creator_id
LEFT JOIN
    board_games AS b
    ON
    cb.board_game_id = b.id
WHERE
    b.id IS NULL
;