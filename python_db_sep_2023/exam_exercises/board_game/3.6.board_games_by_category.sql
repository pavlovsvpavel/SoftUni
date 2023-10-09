SELECT
    b.id,
    b.name,
    b.release_year,
    c.name
FROM
    board_games AS b
INNER JOIN
    categories AS c
    ON
    b.category_id = c.id
WHERE
    c.name IN ('Strategy Games', 'Wargames')
ORDER BY
    b.release_year DESC
;

