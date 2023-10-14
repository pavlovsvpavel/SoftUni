UPDATE coaches
SET salary = salary * coach_level
WHERE
    SUBSTRING(first_name FROM 1 FOR 1) = 'C'
    AND
    (
    SELECT
        COUNT(pc.player_id)
    FROM
        coaches AS c
    INNER JOIN
        players_coaches AS pc
        ON
        c.id = pc.coach_id
    ) >= 1
;