CREATE OR REPLACE FUNCTION fn_creator_with_board_games(
    IN creator_first_name VARCHAR(30),
    OUT num_of_board_games INT
    )
RETURNS INT
AS

$$
BEGIN
    SELECT
        COUNT(c.*)
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
        c.first_name = creator_first_name
    INTO num_of_board_games;
END;
$$
LANGUAGE plpgsql;

-- SELECT fn_creator_with_board_games('Bruno');
-- SELECT fn_creator_with_board_games('Alexander')
