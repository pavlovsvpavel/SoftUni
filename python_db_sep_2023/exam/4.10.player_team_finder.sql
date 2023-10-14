CREATE OR REPLACE PROCEDURE sp_players_team_name(
    IN player_name VARCHAR(50),
    OUT final_result VARCHAR(45)
)
AS
$$
    BEGIN
        SELECT
            t.name
        FROM
            players AS p
        INNER JOIN
            teams AS t
            ON
            p.team_id = t.id
        WHERE
            CONCAT_WS(' ', p.first_name, p.last_name) = player_name
        INTO final_result;
        IF final_result IS NULL THEN
            final_result := 'The player currently has no team';
        END IF;

        RAISE NOTICE '%', final_result;
    END;
$$
LANGUAGE plpgsql;

CALL sp_players_team_name('Thor Serrels', '');
CALL sp_players_team_name('Walther Olenchenko', '');
CALL sp_players_team_name('Isaak Duncombe', '')
