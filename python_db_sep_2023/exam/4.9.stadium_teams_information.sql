CREATE OR REPLACE FUNCTION fn_stadium_team_name(
    IN stadium_name VARCHAR(30)
    )
RETURNS TABLE (
        team_name VARCHAR(30)
        )
AS
$$
    BEGIN
        RETURN QUERY
        SELECT
            t.name
        FROM
            stadiums AS s
        INNER JOIN
            teams AS t
            ON
            s.id = t.stadium_id
        WHERE
            s.name = stadium_name
        ORDER BY
            t.name;
    END;
$$
LANGUAGE plpgsql;

-- SELECT fn_stadium_team_name('BlogXS');
-- SELECT fn_stadium_team_name('Quaxo');
-- SELECT fn_stadium_team_name('Jaxworks')