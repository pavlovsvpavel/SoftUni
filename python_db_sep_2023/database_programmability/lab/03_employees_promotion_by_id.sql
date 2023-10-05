CREATE PROCEDURE sp_increase_salary_by_id(id INT)
AS
$$
BEGIN
    IF (
    SELECT
        e.salary
    FROM
        employees AS e
    WHERE
        e.employee_id = id
    ) IS NULL THEN
    ROLLBACK;

    ELSE
        UPDATE employees as e
        SET salary = salary * 1.05
        WHERE
            e.employee_id = id;
    END IF;
    COMMIT;
END;
$$
LANGUAGE plpgsql;

-- CALL sp_increase_salary_by_id(17);
--
-- SELECT
--     employee_id,
--     salary
-- FROM
--     employees
-- WHERE
--     employee_id = 17