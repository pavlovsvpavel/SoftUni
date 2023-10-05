CREATE OR REPLACE FUNCTION fn_count_employees_by_town(town_name VARCHAR(20))
RETURNS INT AS

$$
DECLARE
    count_of_employees INT;
BEGIN
    SELECT
        COUNT(e.employee_id)
    FROM
        employees AS e
    INNER JOIN
            addresses AS a
    USING (address_id)
    INNER JOIN
            towns AS t
    USING (town_id)
    WHERE
        t.name = town_name
    INTO count_of_employees;
    RETURN count_of_employees;
END;
$$
LANGUAGE plpgsql;

-- SELECT fn_count_employees_by_town('Sofia') AS count;