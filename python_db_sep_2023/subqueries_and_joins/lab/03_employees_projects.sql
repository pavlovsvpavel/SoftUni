SELECT
    e.employee_id,
    CONCAT_WS(' ', e.first_name, e.last_name) as full_name,
    p.project_id,
    p.name AS project_name
FROM
    employees AS e
INNER JOIN
    employees_projects AS e_p
    ON e.employee_id = e_p.employee_id
INNER JOIN
    projects AS p
    ON p.project_id = e_p.project_id
WHERE
    e_p.project_id = 1;