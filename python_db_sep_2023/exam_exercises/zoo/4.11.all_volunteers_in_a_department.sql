CREATE OR REPLACE FUNCTION
    fn_get_volunteers_count_from_department(
    IN searched_volunteers_department VARCHAR(30),
    OUT count_volunteers INT
    )
RETURNS INT
AS
$$
BEGIN
    count_volunteers := (
    SELECT
        COUNT(*)
    FROM volunteers AS v
    INNER JOIN
        volunteers_departments AS vd
    ON
        v.department_id = vd.id
    WHERE
        vd.department_name = searched_volunteers_department
    );
END;
$$
LANGUAGE plpgsql;

-- SELECT fn_get_volunteers_count_from_department('Education program assistant');
-- SELECT fn_get_volunteers_count_from_department('Guest engagement');
-- SELECT fn_get_volunteers_count_from_department('Zoo events')

