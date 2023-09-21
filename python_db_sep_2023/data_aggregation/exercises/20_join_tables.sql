SELECT
    *
FROM
    departments AS d
INNER JOIN
        employees AS e ON d.id = e.department_id;
