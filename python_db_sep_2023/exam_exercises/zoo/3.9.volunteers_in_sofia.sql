SELECT
    name AS "Volunteers Name",
    phone_number AS "Phone Number",
    REGEXP_REPLACE(address, '^\s*Sofia\s*,\s*', '') AS "Address"
FROM
    volunteers
WHERE
    department_id = (
        SELECT
            id
        FROM
            volunteers_departments
        WHERE
            department_name = 'Education program assistant'
        )
    AND
    address LIKE '%Sofia%'

ORDER BY
    "Volunteers Name"
;
