CREATE OR REPLACE FUNCTION fn_difficulty_level (
    IN input_level INT,
    OUT difficulty_level VARCHAR(50)
    )
RETURNS VARCHAR
AS
$$
BEGIN
    IF input_level <= 40 THEN difficulty_level := 'Normal Difficulty';
    ELSIF input_level BETWEEN 40 AND 60 THEN difficulty_level := 'Nightmare Difficulty';
    ELSE difficulty_level := 'Hell Difficulty';
    END IF;
END;
$$
LANGUAGE plpgsql;

SELECT
    user_id,
    level,
    cash,
    fn_difficulty_level(level) AS difficulty_level
FROM
    users_games
ORDER BY
    user_id;