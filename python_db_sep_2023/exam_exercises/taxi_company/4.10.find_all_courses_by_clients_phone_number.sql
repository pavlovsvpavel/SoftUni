CREATE OR REPLACE FUNCTION fn_courses_by_client(
    IN phone_num VARCHAR(20),
    OUT num_of_courses INT
    )
RETURNS INT
AS

$$
BEGIN
    num_of_courses := (
    SELECT
        COUNT(*)
    FROM
        courses AS c
    INNER JOIN
        clients AS cl
        ON
        cl.id = c.client_id
    WHERE
        cl.phone_number = phone_num
    );
END;
$$
LANGUAGE plpgsql;

SELECT fn_courses_by_client('(803) 6386812');
SELECT fn_courses_by_client('(831) 1391236');
SELECT fn_courses_by_client('(704) 2502909')
